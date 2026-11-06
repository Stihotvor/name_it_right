---
status: new
---

# Machine learning

!!! success "General patterns"

    - Name an experiment for the question it answers, and a run for one try: `experiment`, `run`
    - Name a model for what it predicts, and a model version for one trained copy: `churn_classifier`, `churn_classifier` version `7`
    - Keep the data, the code and the result of a run apart: `dataset_version`, `git_commit`, `metric`
    - Name a metric with its split: `val_accuracy`, `test_auc`
    - Name a feature for the thing and the window: `customer_orders_count_30d`

!!! tip "Useful tips"

    - Use `snake_case` for parameters and metrics. MLflow accepts many characters, but a plain name is easy to query
    - Use `X_train`, `y_train` only inside a short function. Use full names for fields that you store
    - Use `dataset_version` and a hash, not `data_v2_final`
    - Use an alias such as `champion` for the version that serves traffic. MLflow aliases replace the older stages

!!! danger "General anti-patterns"

    - `model` for the code, the weights and the service at once
    - `data2`, `data_new`, `final_final`
    - `acc` and `accuracy` for different things in two runs
    - A metric with no split: `loss`
    - `prod` as a model name

The words follow MLflow Tracking and the MLflow Model Registry: `Experiment`, `Run`, `Param`, `Metric`, `Artifact`, `Registered Model`, `Model Version`. MLflow run statuses are `RUNNING`, `SCHEDULED`, `FINISHED`, `FAILED` and `KILLED`. The model version stages `None`, `Staging`, `Production` and `Archived` are deprecated in favor of aliases and tags.

## Entities

| Entity | Meaning | Table | Notes |
|---|---|---|---|
| Experiment | A group of runs for one question. | `experiments` | MLflow `Experiment`. |
| Run | One execution of training or evaluation. | `runs` | MLflow `Run`. |
| Parameter | An input value of a run. | `run_params` | A key and a value. |
| Metric | A number that a run measures. | `run_metrics` | A key, a value, a step, a time. |
| Tag | A label on a run or a model. | `run_tags` | |
| Artifact | A file that a run makes. | `artifacts` | A plot, a model file. |
| Dataset | A named source of data. | `datasets` | |
| Dataset version | A fixed snapshot of a dataset. | `dataset_versions` | Has a hash. |
| Feature | A column that a model reads. | `features` | |
| Feature view | A group of features with one source. | `feature_views` | |
| Label | The true answer for an example. | `labels` | |
| Training job | A job that runs training. | `training_jobs` | |
| Pipeline | A list of steps that make a model. | `pipelines` | |
| Model | A named model in the registry. | `models` | MLflow: registered model. |
| Model version | One trained copy of a model. | `model_versions` | A number, 1, 2, 3. |
| Model alias | A name that points to a version. | `model_aliases` | `champion`, `challenger`. |
| Evaluation | A test of a model version on a dataset. | `evaluations` | |
| Deployment | A model version that runs in an environment. | `deployments` | |
| Endpoint | The address that serves predictions. | `endpoints` | |
| Prediction | One answer of a model. | `predictions` | Often not stored in a database. |
| Drift report | A report on the change of data. | `drift_reports` | |
| Prompt | A text template for a language model. | `prompts` | |

MLflow keeps experiments, runs, parameters, metrics and tags in its own store. The tables above matter only if you mirror them. The worked example keeps only the registry link.

## States

| Entity | States |
|---|---|
| Run (MLflow) | `RUNNING`, `SCHEDULED`, `FINISHED`, `FAILED`, `KILLED` |
| Model version (MLflow) | `PENDING_REGISTRATION`, `FAILED_REGISTRATION`, `READY` |
| Model version stage (deprecated in MLflow) | `None`, `Staging`, `Production`, `Archived` |
| Training job | `queued`, `running`, `succeeded`, `failed`, `canceled` |
| Deployment | `creating`, `ready`, `degraded`, `failed`, `retiring`, `retired` |
| Dataset version | `draft`, `validated`, `deprecated` |

MLflow writes these states in upper case. If you mirror MLflow exactly, keep its values. Otherwise store lower case (`ready`) and map at the boundary. The worked example below keeps the MLflow values. The deployment states are the choice of this guide and are lower case. A training job maps to a run: `running` to `RUNNING`, `succeeded` to `FINISHED`, `failed` to `FAILED`, `canceled` to `KILLED`.

## Actions

| Action | Function name | Meaning | Trap |
|---|---|---|---|
| Start a run | `mlflow.start_run` | Opens a run. | Use it as a context manager. |
| Log a parameter | `mlflow.log_param` | Stores an input value. | A param is a string. |
| Log a metric | `mlflow.log_metric` | Stores a number. | Add a `step` for a curve. |
| Log an artifact | `mlflow.log_artifact` | Stores a file. | |
| Log a model | `mlflow.<flavor>.log_model` | Stores a model in a run. For example `mlflow.sklearn.log_model`. | It is registered only if you pass `registered_model_name`. |
| Register a model | `mlflow.register_model` | Adds a version to the registry. | |
| Fit | `fit` | Trains on data. | Not `train_model` in a class that has `fit`. |
| Predict | `predict` | Gives an answer. | `predict_proba` gives a probability. |
| Evaluate | `evaluate_model` | Measures on a test set. | Do not use the training set. |
| Split | `split_dataset` | Makes train, validation and test sets. | Fix the random seed. |
| Promote | `MlflowClient.set_registered_model_alias` | Points an alias to a version. | The old term is a stage transition. |
| Deploy | `deploy_model_version` | Starts serving. | |
| Roll back | `rollback_deployment` | Returns to the last good version. | |
| Detect drift | `detect_drift` | Compares live data to training data. | |

Names with the `mlflow.` prefix or `MlflowClient` are MLflow APIs. The other names are wrappers in your own application.

## Traps

| Trap | Why it is a problem | Better |
|---|---|---|
| `model` | Code, weights and service are different. | `model` for the registry name, `model_version` for the weights, `endpoint` for the service. |
| `experiment` and `run` | A run is one try. An experiment is the group. | `experiment_id`, `run_id`. |
| `loss` | Training or validation? | `train_loss`, `val_loss`. |
| `acc` and `accuracy` | Two names in two runs. | `accuracy` with a split: `val_accuracy`. |
| `data_v2_final` | The name tells nothing and the file can change. | `dataset_version` with a hash. |
| `train`, `test`, `val`, `eval`, `dev` | Names for splits vary. | `train`, `validation`, `test` in stored fields. `val_` only as a metric prefix. |
| `X` and `y` | Fine in a formula, vague in a field. | `features` and `labels` in stored fields. |
| `feature` | A column, a feature view or a flag? | `feature` for the model input. A [feature flag](../systems/feature-flags.md) is a different thing. |
| `prod` | An environment or a version? | `production` environment, and an alias `champion`. |
| `stage` | Pipeline stage or model stage? | `pipeline_step` and `model_alias`. |
| `target`, `label`, `y` | Three words for the answer. | `label` for a stored true answer, `target` for the column name in a training table. |
| `score` | A probability, a metric or a ranking? | `predicted_probability`, `metric_value`, `ranking_score`. |
| `seed` | Which one? | `split_seed` for a split, `training_seed` for the model. |

## Worked example

```sql
CREATE TABLE model_versions (
    id                  bigint GENERATED ALWAYS AS IDENTITY,
    model_id            bigint NOT NULL,
    version_number      integer NOT NULL,
    run_id              text,
    dataset_version_id  bigint NOT NULL,
    git_commit          text NOT NULL,
    status              text NOT NULL DEFAULT 'READY',
    created_at          timestamptz NOT NULL DEFAULT now(),
    CONSTRAINT pk_model_versions PRIMARY KEY (id),
    CONSTRAINT chk_model_versions_status_allowed CHECK (status IN ('PENDING_REGISTRATION', 'FAILED_REGISTRATION', 'READY')),
    CONSTRAINT uq_model_versions_model_id_version_number UNIQUE (model_id, version_number),
    CONSTRAINT uq_model_versions_model_id_id UNIQUE (model_id, id),
    CONSTRAINT fk_model_versions_models FOREIGN KEY (model_id) REFERENCES models (id),
    CONSTRAINT fk_model_versions_dataset_versions FOREIGN KEY (dataset_version_id) REFERENCES dataset_versions (id)
);

CREATE INDEX idx_model_versions_dataset_version_id ON model_versions (dataset_version_id);

CREATE TABLE model_aliases (
    model_id            bigint NOT NULL,
    alias               text NOT NULL,
    model_version_id    bigint NOT NULL,
    CONSTRAINT pk_model_aliases PRIMARY KEY (model_id, alias),
    CONSTRAINT fk_model_aliases_models FOREIGN KEY (model_id) REFERENCES models (id),
    CONSTRAINT fk_model_aliases_model_versions FOREIGN KEY (model_id, model_version_id) REFERENCES model_versions (model_id, id)
);

CREATE INDEX idx_model_aliases_model_id_model_version_id ON model_aliases (model_id, model_version_id);
```

The tables `models` and `dataset_versions` are not shown. The column `run_id` points into the MLflow tracking server, so it has no foreign key. A version can exist without a run.

```py
import mlflow


def train_churn_classifier(dataset_version: str, learning_rate: float) -> str:
    mlflow.set_experiment("churn_prediction")
    with mlflow.start_run(run_name="churn_classifier") as run:
        mlflow.log_param("dataset_version", dataset_version)
        mlflow.log_param("git_commit", current_git_commit())
        mlflow.log_param("learning_rate", learning_rate)
        model = fit_classifier(dataset_version, learning_rate)
        mlflow.log_metric("val_accuracy", evaluate_accuracy(model, split="validation"))
        mlflow.log_metric("val_auc", evaluate_auc(model, split="validation"))
        mlflow.sklearn.log_model(model, name="model", registered_model_name="churn_classifier")
        return run.info.run_id
```

```
POST /v1/models/{model_id}/versions                   register a version
PUT  /v1/models/{model_id}/aliases/{alias}            point an alias to a version
POST /v1/deployments                                  deploy a model version
POST /v1/endpoints/{endpoint_id}:predict           get predictions
```

```
ModelVersionRegistered   ModelAliasSet   DeploymentActivated   DriftDetected   DeploymentRolledBack
```

## Related patterns

- [Booleans, collections, units and time](../patterns/booleans-collections-units-time.md) for units and split names
- [Observability](../systems/observability.md) for metric names such as `val_accuracy`
- [Python variables](../python/variables.md) for `snake_case` names of parameters and metrics

!!! info "See also"

    - [Examples overview](index.md), [Python variables](../python/variables.md), [Tables](../databases/tables.md) and [Observability](../systems/observability.md)
    - [MLflow Tracking](https://mlflow.org/docs/latest/ml/tracking/), [MLflow Model Registry](https://mlflow.org/docs/latest/ml/model-registry/)
