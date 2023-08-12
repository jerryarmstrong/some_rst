.github/PULL_REQUEST_TEMPLATE.md
================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: md

    *Replace this paragraph with a description of what this PR is changing or adding, and why. Consider including before/after screenshots.*

*List which issues are fixed by this PR. You must list at least one issue.*

*If you had to change anything in the [flutter/tests] repo, include a link to the migration guide as per the [breaking change policy].*

## Pre-launch Checklist

- [ ] I read the [Contributor Guide] and followed the process outlined there for submitting PRs.
- [ ] I read the [Tree Hygiene] wiki page, which explains my responsibilities.
- [ ] I read and followed the [relevant style guides] and ran [the auto-formatter]. (Unlike the flutter/flutter repo, the flutter/plugins repo does use `dart format`.)
- [ ] I signed the [CLA].
- [ ] The title of the PR starts with the name of the plugin surrounded by square brackets, e.g. `[shared_preferences]`
- [ ] I listed at least one issue that this PR fixes in the description above.
- [ ] I updated `pubspec.yaml` with an appropriate new version according to the [pub versioning philosophy], or this PR is [exempt from version changes].
- [ ] I updated `CHANGELOG.md` to add a description of the change, [following repository CHANGELOG style].
- [ ] I updated/added relevant documentation (doc comments with `///`).
- [ ] I added new tests to check the change I am making, or this PR is [test-exempt].
- [ ] All existing and new tests are passing.

If you need help, consider asking for advice on the #hackers-new channel on [Discord].

<!-- Links -->
[Contributor Guide]: https://github.com/flutter/plugins/blob/main/CONTRIBUTING.md
[Tree Hygiene]: https://github.com/flutter/flutter/wiki/Tree-hygiene
[relevant style guides]: https://github.com/flutter/plugins/blob/main/CONTRIBUTING.md#style
[CLA]: https://cla.developers.google.com/
[flutter/tests]: https://github.com/flutter/tests
[breaking change policy]: https://github.com/flutter/flutter/wiki/Tree-hygiene#handling-breaking-changes
[Discord]: https://github.com/flutter/flutter/wiki/Chat
[pub versioning philosophy]: https://dart.dev/tools/pub/versioning
[exempt from version changes]: https://github.com/flutter/flutter/wiki/Contributing-to-Plugins-and-Packages#version-and-changelog-updates
[following repository CHANGELOG style]: https://github.com/flutter/flutter/wiki/Contributing-to-Plugins-and-Packages#changelog-style
[the auto-formatter]: https://github.com/flutter/plugins/blob/main/script/tool/README.md#format-code
[test-exempt]: https://github.com/flutter/flutter/wiki/Tree-hygiene#tests


