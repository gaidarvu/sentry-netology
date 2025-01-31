import sentry_sdk

sentry_sdk.init(
    dsn="https://f2e281c651a4c2cb0b5088a01a0631f2@o4508738381217792.ingest.de.sentry.io/4508738530115664",
    environment="development",
    release="1.0"
)

if __name__ == "__main__":
    division_zero = 1 /0
