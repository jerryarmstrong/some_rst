README.md
=========

Last edited: 2018-09-14 20:25:17

Contents:

.. code-block:: md

    <h1><img alt="Elastic CI Stack for AWS" src="https://cdn.rawgit.com/buildkite/elastic-ci-stack-for-aws/master/images/banner.png"></h1>

![Build status](https://badge.buildkite.com/d178ab942e2f606a83e79847704648437d82a9c5fdb434b7ae.svg?branch=master)

The Buildkite Elastic CI Stack gives you a private, autoscaling [Buildkite Agent](https://buildkite.com/docs/agent) cluster. Use it to parallelize legacy tests across hundreds of nodes, run tests and deployments for all your Linux-based services and apps, or run AWS ops tasks.

**For documentation on a [release](https://github.com/buildkite/elastic-ci-stack-for-aws/releases), such as [the latest stable release](https://github.com/buildkite/elastic-ci-stack-for-aws/releases/latest), please see its _Documentation_ section.**

Features:

- All major AWS regions
- Configurable instance size
- Configurable number of buildkite agents per instance
- Configurable spot instance bid price
- Configurable auto-scaling based on build activity
- Docker and Docker Compose support
- Per-pipeline S3 secret storage (with SSE encryption support)
- Docker Registry push/pull support
- CloudWatch logs for system and buildkite agent events
- CloudWatch metrics from the Buildkite API
- Support for stable, beta or edge Buildkite Agent releases
- Create as many instances of the stack as you need
- Rolling updates to stack instances to reduce interruption

## Contents

<!-- toc -->

- [Getting Started](#getting-started)
- [Build Secrets](#build-secrets)
- [What’s On Each Machine?](#whats-on-each-machine)
- [What Type of Builds Does This Support?](#what-type-of-builds-does-this-support)
- [Multiple Instances of the Stack](#multiple-instances-of-the-stack)
- [Autoscaling](#autoscaling)
- [Docker Registry Support](#docker-registry-support)
- [Versions](#versions)
- [Updating Your Stack](#updating-your-stack)
- [CloudWatch Metrics](#cloudwatch-metrics)
- [Reading Instance and Agent Logs](#reading-instance-and-agent-logs)
- [Optimizing for Slow Docker Builds](#optimizing-for-slow-docker-builds)
- [Security](#security)
- [Development](#development)
- [Questions and Support](#questions-and-support)
- [Licence](#licence)

<!-- tocstop -->

## Getting Started

See the [Elastic CI Stack for AWS guide](https://buildkite.com/docs/guides/elastic-ci-stack-aws) for a step-by-step guide, or jump straight in:

[![Launch AWS Stack](https://cdn.rawgit.com/buildkite/cloudformation-launch-stack-button-svg/master/launch-stack.svg)](https://console.aws.amazon.com/cloudformation/home#/stacks/new?stackName=buildkite&templateURL=https://s3.amazonaws.com/buildkite-aws-stack/latest/aws-stack.json)

Current release is ![](https://img.shields.io/github/release/buildkite/elastic-ci-stack-for-aws.svg). See [Releases](https://github.com/buildkite/elastic-ci-stack-for-aws/releases) for older releases, or [Versions](#versions) for development version

> Although the stack will create it's own VPC by default, we highly recommend following best practice by setting up a separate development AWS account and using role switching and consolidated billing—see the [Delegate Access Across AWS Accounts tutorial](http://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html) for more information.

If you'd like to use the [AWS CLI](https://aws.amazon.com/cli/), download [`config.json.example`](config.json.example), rename it to `config.json`, and then run the below command:

```bash
aws cloudformation create-stack \
  --output text \
  --stack-name buildkite \
  --template-url "https://s3.amazonaws.com/buildkite-aws-stack/latest/aws-stack.json" \
  --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM \
  --parameters $(cat config.json)
```

## Build Secrets

The stack will have created an S3 bucket for you (or used the one you provided as the `SecretsBucket` parameter). This will be where the agent will fetch your SSH private keys for source control, and environment hooks to provide other secrets to your builds.

The following s3 objects are downloaded and processed:

* `/env` - An [agent environment hook](https://buildkite.com/docs/agent/hooks)
* `/private_ssh_key` - A private key that is added to ssh-agent for your builds
* `/git-credentials` - A [git-credentials](https://git-scm.com/docs/git-credential-store#_storage_format) file for git over https
* `/{pipeline-slug}/env` - An [agent environment hook](https://buildkite.com/docs/agent/hooks), specific to a pipeline
* `/{pipeline-slug}/private_ssh_key` - A private key that is added to ssh-agent for your builds, specific to the pipeline
* `/{pipeline-slug}/git-credentials` - A [git-credentials](https://git-scm.com/docs/git-credential-store#_storage_format) file for git over https, specific to a pipeline

These files are encrypted using [Amazon's KMS Service](https://aws.amazon.com/kms/). See the [Security](#security) section for more details.

Here's an example that shows how to generate a private SSH key, and upload it with KMS encryption to an S3 bucket:

```bash
# generate a deploy key for your project
ssh-keygen -t rsa -b 4096 -f id_rsa_buildkite
pbcopy < id_rsa_buildkite.pub # paste this into your github deploy key

aws s3 cp --acl private --sse aws:kms id_rsa_buildkite "s3://${SecretsBucket}/private_ssh_key"
```

If you want to set secrets that your build can access, create a file that sets environment variables and upload it:

```bash
echo "export MY_ENV_VAR=something secret" > myenv
aws s3 cp --acl private --sse aws:kms myenv "s3://${SecretsBucket}/env"
rm myenv
```

**Note: Currently only using the default KMS key for s3 can be used, follow [#235](https://github.com/buildkite/elastic-ci-stack-for-aws/issues/235) for progress on using specific KMS keys**

If you really want to store your secrets unencrypted, you can disable it entirely with `BUILDKITE_USE_KMS=false`.

## What’s On Each Machine?

* [Amazon Linux 2017.09.1](https://aws.amazon.com/amazon-linux-ami/)
* [Buildkite Agent](https://buildkite.com/docs/agent)
* [Docker 17.12.0-ce](https://www.docker.com)
* [Docker Compose 1.18.0](https://docs.docker.com/compose/)
* [aws-cli](https://aws.amazon.com/cli/) - useful for performing any ops-related tasks
* [jq](https://stedolan.github.io/jq/) - useful for manipulating JSON responses from cli tools such as aws-cli or the Buildkite API

## What Type of Builds Does This Support?

This stack is designed to run your builds in a share-nothing pattern similar to the [12 factor application principals](http://12factor.net):

* Each project should encapsulate it's dependencies via Docker and Docker Compose
* Build pipeline steps should assume no state on the machine (and instead rely on [build meta-data](https://buildkite.com/docs/guides/build-meta-data), [build artifacts](https://buildkite.com/docs/guides/artifacts) or S3)
* Secrets are configured via environment variables exposed using the S3 secrets bucket

By following these simple conventions you get a scaleable, repeatable and source-controlled CI environment that any team within your organization can use.

## Multiple Instances of the Stack

If you need to different instances sizes and scaling characteristics between pipelines, you can create multiple stack. Each can run on a different [Agent Queue](https://buildkite.com/docs/agent/queues), with it's own configuration, or even in a different AWS account.

Examples:

* A `docker-builders` stack that provides always-on workers with hot docker caches (see [Optimizing for Slow Docker Builds](#optimizing-for-slow-docker-builds))
* A `pipeline-uploaders` stack with tiny, always-on instances for lightning fast `buildkite-agent pipeline upload` jobs.
* A `deploy` stack with added credentials and permissions specifically for deployment.

## Autoscaling

If you have configured `MinSize` < `MaxSize`, the stack will automatically scale up and down based on the number of scheduled jobs.

This means you can scale down to zero when idle, which means you can use larger instances for the same cost.

Metrics are collected with a Lambda function, polling every minute.

## Docker Registry Support

If you want to push or pull from registries such as [Docker Hub](https://hub.docker.com/) or [Quay](https://quay.io/) you can use the `environment` hook in your secrets bucket to export the following environment variables:

* `DOCKER_LOGIN_USER="the-user-name"`
* `DOCKER_LOGIN_PASSWORD="the-password"`
* `DOCKER_LOGIN_SERVER=""` - optional. By default it will log into Docker Hub

Setting these will perform a `docker login` before each pipeline step is run, allowing you to `docker push` to them from within your build scripts.

If you are using [Amazon ECR](https://aws.amazon.com/ecr/) you can set the `ECRAccessPolicy` parameter to the stack to either `readonly`, `poweruser`, or `full` depending on [the access level you want](http://docs.aws.amazon.com/AmazonECR/latest/userguide/ecr_managed_policies.html) your builds to have

You can disable this in individual pipelines by setting `AWS_ECR_LOGIN=false`.

If you want to login to an ECR server on another AWS account, you can set `AWS_ECR_LOGIN_REGISTRY_IDS="id1,id2,id3"`.

The AWS ECR options are powered by an embedded version of the [ECR plugin](https://github.com/buildkite-plugins/ecr-buildkite-plugin), so if you require options that aren't listed here, you can disable the embedded version as above and call the plugin directly. See [it's README](https://github.com/buildkite-plugins/ecr-buildkite-plugin) for more examples (requires Agent v3.x).

## Versions

We recommend running the latest release, which is available at `https://s3.amazonaws.com/buildkite-aws-stack/aws-stack.json`, or on the [releases page](https://github.com/buildkite/elastic-ci-stack-for-aws/releases).

The latest build of the stack is published to `https://s3.amazonaws.com/buildkite-aws-stack/master/aws-stack.json`, along with a version for each commit in the form of `https://s3.amazonaws.com/buildkite-aws-stack/master/${COMMIT}.aws-stack.json`.

Branches are published in the form of `https://s3.amazonaws.com/buildkite-aws-stack/${BRANCH}/aws-stack.json`.

## Updating Your Stack

To update your stack to the latest version use CloudFormation’s stack update tools with one of the urls in the [Versions](#versions) section.

Prior to updating, it's a good idea to set the desired instance size on the AutoscalingGroup to 0 manually.

## CloudWatch Metrics

Metrics are calculated every minute from the Buildkite API using a lambda function.

<img width="544" alt="cloudwatch" src="https://cloud.githubusercontent.com/assets/153/16836158/85abdbc6-49ff-11e6-814c-eaf2400e8333.png">

You’ll find the stack’s metrics under "Custom Metrics > Buildkite" within CloudWatch.

## Reading Instance and Agent Logs

Each instance streams both system messages and Buildkite Agent logs to CloudWatch Logs under two log groups:

* `/var/log/messages` - System logs
* `/var/log/buildkite-agent.log` - Buildkite Agent logs
* `/var/log/docker` - Docker daemon logs
* `/var/log/elastic-stack.log` - Boot process logs

Within each stream the logs are grouped by instance id.

To debug an agent first find the instance id from the agent in Buildkite, head to your [CloudWatch Logs Dashboard](https://console.aws.amazon.com/cloudwatch/home?#logs:), choose either the system or Buildkite Agent log group, and then search for the instance id in the list of log streams.

## Optimizing for Slow Docker Builds

For large legacy applications the Docker build process might take a long time on new instances. For these cases it’s recommended to create an optimized "builder" stack which doesn't scale down, keeps a warm docker cache and is responsible for building and pushing the application to Docker Hub before running the parallel build jobs across your normal CI stack.

An example of how to set this up:

1. Create a Docker Hub repository for pushing images to
1. Update the pipeline’s `env` hook in your secrets bucket to perform a `docker login`
1. Create a builder stack with its own queue (i.e. `elastic-builders`), making sure to use `beta` agents so you can use the [Docker Compose Buildkite Plugin](https://github.com/buildkite-plugins/docker-compose-buildkite-plugin) and [pre-building](https://github.com/buildkite-plugins/docker-compose-buildkite-plugin#pre-building-the-image)

Here is an example build pipeline based on a production Rails application:

```yaml
steps:
  - name: ":docker: :package:"
    plugins:
      docker-compose:
        build: app
        image-repository: my-docker-org/my-repo
    agents:
      queue: elastic-builders
  - wait
  - name: ":hammer:"
    command: ".buildkite/steps/tests"
    plugins:
      docker-compose:
        run: app
    agents:
      queue: elastic
    parallelism: 75
```

See [Issue 81](https://github.com/buildkite/elastic-ci-stack-for-aws/issues/81) for ideas on other solutions (contributions welcome!).

## Security

This repository hasn't been reviewed by security researchers so exercise caution and careful thought with what credentials you make available to your builds.

Anyone with commit access to your codebase (including third-party pull-requests if you've enabled them in Buildkite) will have access to your secrets bucket files.

Also keep in mind the EC2 HTTP metadata server is available from within builds, which means builds act with the same IAM permissions as the instance.

## Development

To get started with customizing your own stack, or contributing fixes and features:

```bash
# Build an AMI
make build

# Or, to set things up locally and create the stack on AWS
make create-stack

# You can use any of the AWS* environment variables that the aws-cli supports
AWS_PROFILE="some-profile" make create-stack

# You can also use aws-vault or similar
aws-vault exec some-profile -- make create-stack
```

If you need to build your own AMI (because you've changed something in the `packer` directory), run:

```bash
make clean build-ami
```

## Questions and Support

Feel free to drop an email to support@buildkite.com with questions. It helps us if you can provide the following details:

```
# List your stack parameters
aws cloudformation describe-stacks --stack-name MY_STACK_NAME \
  --query 'Stacks[].Parameters[].[ParameterKey,ParameterValue]' --output table
```

Provide us with logs from Cloudwatch Logs:

```
/buildkite/elastic-stack-init/{instance-id}
/buildkite/docker-daemon/{instance-id}
```

Alternately, drop by `#aws-stack` and `#aws` channels in [Buildkite Community Slack](https://chat.buildkite.com/) and ask your question!

## Licence

See [Licence.md](Licence.md) (MIT)


