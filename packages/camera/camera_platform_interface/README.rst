packages/camera/camera_platform_interface/README.md
===================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: md

    # camera_platform_interface

A common platform interface for the [`camera`][1] plugin.

This interface allows platform-specific implementations of the `camera`
plugin, as well as the plugin itself, to ensure they are supporting the
same interface.

# Usage

To implement a new platform-specific implementation of `camera`, extend
[`CameraPlatform`][2] with an implementation that performs the
platform-specific behavior, and when you register your plugin, set the default
`CameraPlatform` by calling
`CameraPlatform.instance = MyPlatformCamera()`.

# Note on breaking changes

Strongly prefer non-breaking changes (such as adding a method to the interface)
over breaking changes for this package.

See https://flutter.dev/go/platform-interface-breaking-changes for a discussion
on why a less-clean interface is preferable to a breaking change.

[1]: ../camera
[2]: lib/camera_platform_interface.dart


