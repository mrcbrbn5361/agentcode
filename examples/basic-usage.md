# Basic Usage Examples

This guide provides practical examples of using AgentCode.

---

## Example 1: Quick Code Generation

### Scenario
User needs a Python function quickly.

### Input
```
Write a Python function to calculate factorial
```

### AgentCode Analysis
- **Task Type**: Quick code generation
- **Recommended Model**: DeepSeek V4 Flash
- **Reason**: Fastest at 126 tokens/s

### Output
```python
def factorial(n):
    """Calculate factorial of a number."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120
```

---

## Example 2: Image Analysis

### Scenario
User has a UI bug and provides a screenshot.

### Input
```
What's wrong with this UI? [attaches screenshot]
```

### AgentCode Analysis
- **Task Type**: Multimodal (image analysis)
- **Recommended Model**: MiMo-V2.5
- **Reason**: Native image understanding

### Output
```
I can see the issue in your UI:

1. **Button Overlap**: The submit button is overlapping with the text label
2. **Padding Issue**: Current padding is 8px, should be 16px
3. **Color Contrast**: Button color doesn't meet WCAG AA standards

Here's the fix:
```css
.submit-button {
  padding: 16px 24px;
  margin-top: 16px;
  background-color: #007bff;
  color: #ffffff;
}
```

---

## Example 3: Terminal Task

### Scenario
User needs a Docker configuration.

### Input
```
Create a Docker compose file for a Node.js app with PostgreSQL and Redis
```

### AgentCode Analysis
- **Task Type**: Terminal/CLI task
- **Recommended Model**: Laguna S 2.1
- **Reason**: Terminal-Bench 70.2%

### Output
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
      - REDIS_URL=redis://redis:6379
    depends_on:
      - db
      - redis

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

---

## Example 4: Large Codebase Analysis

### Scenario
User has a large codebase and needs architectural review.

### Input
```
Analyze this 50,000 line codebase and suggest improvements
```

### AgentCode Analysis
- **Task Type**: Large context analysis
- **Recommended Model**: Nemotron 3 Ultra
- **Reason**: 1M context window

### Output
```
## Architecture Analysis

### Current State
- 50,000 lines across 120 files
- Monolithic structure with tight coupling
- Test coverage: 65%

### Recommendations

#### 1. Modularization (High Priority)
- Split into microservices: auth, payments, notifications
- Estimated effort: 2-3 weeks
- Impact: Improved maintainability

#### 2. Database Optimization (Medium Priority)
- Add connection pooling
- Implement read replicas
- Estimated effort: 1 week
- Impact: Better performance

#### 3. Error Handling (Low Priority)
- Standardize error responses
- Add comprehensive logging
- Estimated effort: 3 days
- Impact: Better debugging
```

---

## Example 5: Local Deployment

### Scenario
User needs to process sensitive code locally.

### Input
```
Analyze this code locally without sending to cloud
```

### AgentCode Analysis
- **Task Type**: Sovereign AI requirement
- **Recommended Model**: North Mini Code
- **Reason**: Runs on your machine

### Output
```
Analysis completed locally.
No data was sent to external servers.
All processing happened on your device.

Results: [analysis output]
```

---

## Example 6: Budget-Conscious Processing

### Scenario
User needs to process many files at low cost.

### Input
```
Process 1000 CSV files and extract summary statistics
```

### AgentCode Analysis
- **Task Type**: High-volume processing
- **Recommended Model**: Ling-3.0-flash
- **Reason**: Most token-efficient

### Output
```
Processing 1000 files...
Using cost-efficient model: Ling-3.0-flash

Results:
- Files processed: 1000
- Total rows: 1,234,567
- Summary statistics generated
- Cost: Minimal (free tier)
```

---

## Example 7: Quick Planning

### Scenario
User needs to plan a feature implementation.

### Input
```
Plan the implementation of a user authentication system
```

### AgentCode Analysis
- **Task Type**: Planning and analysis
- **Recommended Model**: Big Pickle
- **Reason**: Free and fast

### Output
```
## Authentication System Plan

### Components
1. User registration
2. Login/logout
3. Password reset
4. Session management
5. OAuth integration

### Database Schema
- users table
- sessions table
- oauth_tokens table

### API Endpoints
- POST /auth/register
- POST /auth/login
- POST /auth/logout
- POST /auth/reset-password

### Implementation Order
1. User registration (2 days)
2. Login/logout (1 day)
3. Session management (1 day)
4. Password reset (1 day)
5. OAuth integration (2 days)

Total estimated time: 7 days
```

---

## Model Selection Summary

| Task Type | Best Model | Why |
|-----------|------------|-----|
| Quick code | DeepSeek V4 Flash | 126 tok/s |
| Image analysis | MiMo-V2.5 | Multimodal |
| Terminal tasks | Laguna S 2.1 | Terminal expert |
| Large context | Nemotron 3 Ultra | 1M tokens |
| Local processing | North Mini Code | Sovereign AI |
| Budget tasks | Ling-3.0-flash | Efficient |
| Planning | Big Pickle | Free |

---

## Tips

1. **Be specific** in your requests
2. **Provide context** when possible
3. **Specify requirements** (speed, cost, privacy)
4. **Review outputs** before using
5. **Verify model selection** matches your needs

---

For more examples, see the main [README.md](../README.md).
