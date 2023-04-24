??? success "General patterns"
    
    - Use CamelCase in the class names  
    - The class represents an object with a complex, encapsulated (or not) functionality. Use nouns to reflect it.
    
??? tip "Useful tips"  

    - Use a consistent naming convention throughout your code, so it's easy to understand and navigate. If you're 
      working on a team, agree on a naming convention to use across all your code.
    - Class names should be concise and easy to type, but also descriptive enough to convey their purpose. Avoid 
      excessively long names that are difficult to read or type. 
    - Use mnemonics: If your class name is hard to remember or pronounce, consider using a mnemonic or an acronym 
      to help people remember it. Just make sure the mnemonic or acronym is easy to understand and related to 
      the purpose of the class.
    - When choosing a class name, consider the future scalability of your code. Choose a name that can easily 
      accommodate potential future changes or additions to your code, without requiring a complete rewrite.

??? danger "General anti-patterns"
    
    - Avoid using abbreviations in your class names, unless they are commonly understood within your domain. 
      Abbreviations can be confusing and make your code harder to read.

## Naming examples by the context or usecase
### Validation
|           |              |              |               |
| --------- | ------------ | ------------ | ------------- |
| Validator | InputChecker | DataVerifier | FormValidator |
| ParamValidator | RequestValidator | ModelValidator | SchemaValidator |
| InputValidator | VerificationEngine | Verifier | RuleValidator |
| IntegrityValidator | TypeChecker | ValueValidator | ValidationEngine |
| AssertionValidator | ConstraintValidator | DataIntegrityChecker | FormatValidator |

