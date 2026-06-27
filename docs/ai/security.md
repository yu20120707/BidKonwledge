# Python Security Guidance

## Review Focus

- Treat authentication, authorization, session, token, CORS, CSRF, and input-validation changes as high risk.
- Check deserialization, path traversal, SSRF, SQL injection, command injection, pickle usage, and template injection surfaces.
- Do not log secrets, bearer tokens, cookies, passwords, or sensitive request bodies.

## Dependency And Framework Security

- Review dependency updates for CVEs and transitive impact where project tooling supports it.
- For FastAPI, Django, Flask, or Starlette security changes, verify both allowed and denied paths.
- Keep security defaults explicit; avoid relying on incidental framework behavior.

## Verification

- Add negative authorization tests for protected endpoints.
- Record skipped security tests and the reason in `.ai/verification.md` for medium or large work.
