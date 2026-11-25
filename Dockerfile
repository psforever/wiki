# syntax=docker/dockerfile:1

# base: Zensical and the site's Markdown extension. Used by the check service,
# the devcontainer, and CI-style builds, with the checkout mounted at runtime.
FROM python:3.13-slim AS base

WORKDIR /work

# requirements.txt installs the local figure extension from ./src/figure, so
# copy it before installing. Rebuild the image after changing either.
COPY requirements.txt ./
COPY src ./src
RUN pip install --no-cache-dir --disable-pip-version-check --root-user-action=ignore -r requirements.txt

EXPOSE 8000

CMD ["zensical", "serve", "--dev-addr=0.0.0.0:8000"]

# preview: base plus a copy of the site, for `docker compose watch`, which
# syncs edits into this copy so Zensical sees them and live-reloads.
FROM base AS preview

COPY zensical.toml ./
COPY overrides ./overrides
COPY wiki ./wiki
