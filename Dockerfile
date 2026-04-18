FROM python:3.12-slim AS builder

WORKDIR /build

COPY pyproject.toml README.md ./
COPY src/ ./src/

RUN pip install --no-cache-dir --upgrade pip && \
    pip wheel --no-cache-dir --wheel-dir /wheels .


FROM python:3.12-slim AS runtime

# Security: non-root user
RUN useradd --create-home --uid 1000 mcp

WORKDIR /app

COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/*.whl && rm -rf /wheels

USER mcp

# HTTP transport by default; override with FORTIEDR_TRANSPORT=stdio for stdio
ENV FORTIEDR_TRANSPORT=http \
    FORTIEDR_HTTP_HOST=0.0.0.0 \
    FORTIEDR_HTTP_PORT=3000 \
    FORTIEDR_READ_ONLY=true \
    PYTHONUNBUFFERED=1

EXPOSE 3000

# Healthcheck — ensure the MCP endpoint is responsive
HEALTHCHECK --interval=30s --timeout=5s --start-period=15s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:3000/mcp', timeout=3)" || exit 1

ENTRYPOINT ["python", "-m", "fortiedr_mcp"]
