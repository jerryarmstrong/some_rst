packages/camera/camera_android_camerax/android/src/main/java/io/flutter/plugins/camerax/ProcessCameraProviderFlutterApiImpl.java
================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.camerax;

import androidx.camera.lifecycle.ProcessCameraProvider;
import io.flutter.plugin.common.BinaryMessenger;
import io.flutter.plugins.camerax.GeneratedCameraXLibrary.ProcessCameraProviderFlutterApi;

public class ProcessCameraProviderFlutterApiImpl extends ProcessCameraProviderFlutterApi {
  public ProcessCameraProviderFlutterApiImpl(
      BinaryMessenger binaryMessenger, InstanceManager instanceManager) {
    super(binaryMessenger);
    this.instanceManager = instanceManager;
  }

  private final InstanceManager instanceManager;

  void create(ProcessCameraProvider processCameraProvider, Reply<Void> reply) {
    create(instanceManager.addHostCreatedInstance(processCameraProvider), reply);
  }
}


