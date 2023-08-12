packages/camera/camera_android_camerax/android/src/main/java/io/flutter/plugins/camerax/JavaObjectHostApiImpl.java
==================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.camerax;

import androidx.annotation.NonNull;
import io.flutter.plugins.camerax.GeneratedCameraXLibrary.JavaObjectHostApi;

/**
 * A pigeon Host API implementation that handles creating {@link Object}s and invoking its static
 * and instance methods.
 *
 * <p>{@link Object} instances created by {@link JavaObjectHostApiImpl} are used to intercommunicate
 * with a paired Dart object.
 */
public class JavaObjectHostApiImpl implements JavaObjectHostApi {
  private final InstanceManager instanceManager;

  /**
   * Constructs a {@link JavaObjectHostApiImpl}.
   *
   * @param instanceManager maintains instances stored to communicate with Dart objects
   */
  public JavaObjectHostApiImpl(InstanceManager instanceManager) {
    this.instanceManager = instanceManager;
  }

  @Override
  public void dispose(@NonNull Long identifier) {
    instanceManager.remove(identifier);
  }
}


