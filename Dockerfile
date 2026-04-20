FROM python:3.12-slim

# ---- Create non-root user ----
RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser

WORKDIR /app

# ---- Set ownership ----
RUN chown -R appuser:appgroup /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

# ---- change user ----
USER appuser

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080"]