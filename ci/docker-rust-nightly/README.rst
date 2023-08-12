ci/docker-rust-nightly/README.md
================================

Last edited: 2023-08-11 21:38:33

Contents:

.. code-block:: md

    Docker image containing rust nightly and some preinstalled crates used in CI.

This image may be manually updated by running `CI=true ./build.sh` if you are a member
of the [Solana Labs](https://hub.docker.com/u/solanalabs/) Docker Hub
organization.

## Moving to a newer nightly

NOTE: Follow instructions in docker-rust/README.md before this when updating the stable
rust version as well.

We pin the version of nightly (see the `ARG nightly=xyz` line in `Dockerfile`)
to avoid the build breaking at unexpected times, as occasionally nightly will
introduce breaking changes.

To update the pinned version:
1. Edit `Dockerfile` to match the desired stable rust version to base on if needed.
1. Run `ci/docker-rust-nightly/build.sh` to rebuild the nightly image locally,
   or potentially `ci/docker-rust-nightly/build.sh YYYY-MM-DD` if there's a
   specific YYYY-MM-DD that is desired (default is today's build).
   Check https://rust-lang.github.io/rustup-components-history/ for build
   status
1. Update `ci/rust-version.sh` to reflect the new nightly `YYYY-MM-DD`
1. Run `SOLANA_ALLOCATE_TTY=1 SOLANA_DOCKER_RUN_NOSETUID=1 ci/docker-run.sh --nopull solanalabs/rust-nightly:YYYY-MM-DD ci/test-checks.sh`
   and `SOLANA_ALLOCATE_TTY=1 SOLANA_DOCKER_RUN_NOSETUID=1 ci/docker-run.sh --nopull solanalabs/rust-nightly:YYYY-MM-DD ci/test-coverage.sh [args]...`
   to confirm the new nightly image builds.  Fix any issues as needed
1. Run `docker login` to enable pushing images to Docker Hub, if you're authorized.
1. Run `CI=true ci/docker-rust-nightly/build.sh YYYY-MM-DD` to push the new nightly image to dockerhub.com.
1. Send a PR with the `ci/rust-version.sh` change and any codebase adjustments needed.

## Troubleshooting

### Resource is denied

When running `CI=true ci/docker-rust-nightly/build.sh`, you see:

```
denied: requested access to the resource is denied
```

Run `docker login` to enable pushing images to Docker Hub. Contact @mvines or @garious
to get write access.


