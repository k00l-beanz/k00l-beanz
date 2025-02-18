1qaz!QAZ1qaz!QAZ

- challenge/challenge/app/middleware/auth.py
- Only decodes the token, does not verify token
```python
def decode_jwt_token(token):
    try:
        payload = jwt.decode(token, current_app.config["JWT_SECRET_KEY"], algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired."}
    except jwt.InvalidTokenError:
        return None
    except Exception as e:
        print(f"Unexpected error decoding JWT: {str(e)}")  
        return None
```