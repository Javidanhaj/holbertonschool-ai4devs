# API Documentation Prompt Template

**Category:** Documentation  
**Use Case:** API Documentation  
**Role:** API technical writer and backend engineer  
**Task:** Explain an endpoint's contract with examples, errors, and authentication requirements.  
**Input Placeholders:** `[ENDPOINTS]`, `[REQUEST_SCHEMA]`, `[RESPONSE_SCHEMA]`, `[AUTHENTICATION]`, `[ERROR_CODES]`  
**Expected Output Format:** Structured Markdown API reference with endpoint tables and request/response examples.

## Reusable Prompt

Act as a technical writer documenting an existing API. Use only the supplied contract.

**Endpoints (HTTP method and path):** [ENDPOINTS]  
**Request parameters and body schema:** [REQUEST_SCHEMA]  
**Response schema and examples:** [RESPONSE_SCHEMA]  
**Authentication:** [AUTHENTICATION]  
**Known status and error codes:** [ERROR_CODES]

Do not guess undocumented fields, HTTP statuses, or security requirements. Clearly label missing information.

For each endpoint, provide:
1. **Purpose and Method/Path**
2. **Authentication**
3. **Parameters and Request Body:** Markdown tables with required/optional flags.
4. **Example Request and Response:** JSON or shell code blocks based on provided data.
5. **Status Codes and Errors:** Document only supplied cases.
