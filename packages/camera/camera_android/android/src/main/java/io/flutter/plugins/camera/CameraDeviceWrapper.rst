packages/camera/camera_android/android/src/main/java/io/flutter/plugins/camera/CameraDeviceWrapper.java
=======================================================================================================

Last edited: 2023-03-17 07:52:27

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.camera;

import android.annotation.TargetApi;
import android.hardware.camera2.CameraAccessException;
import android.hardware.camera2.CameraCaptureSession;
import android.hardware.camera2.CaptureRequest;
import android.hardware.camera2.params.SessionConfiguration;
import android.os.Build;
import android.os.Handler;
import android.view.Surface;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import java.util.List;

/** A mockable wrapper for CameraDevice calls. */
interface CameraDeviceWrapper {
  @NonNull
  CaptureRequest.Builder createCaptureRequest(int templateType) throws CameraAccessException;

  @TargetApi(Build.VERSION_CODES.P)
  void createCaptureSession(SessionConfiguration config) throws CameraAccessException;

  @TargetApi(Build.VERSION_CODES.LOLLIPOP)
  void createCaptureSession(
      @NonNull List<Surface> outputs,
      @NonNull CameraCaptureSession.StateCallback callback,
      @Nullable Handler handler)
      throws CameraAccessException;

  void close();
}


