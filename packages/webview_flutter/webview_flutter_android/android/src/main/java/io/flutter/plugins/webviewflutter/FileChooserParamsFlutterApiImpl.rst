packages/webview_flutter/webview_flutter_android/android/src/main/java/io/flutter/plugins/webviewflutter/FileChooserParamsFlutterApiImpl.java
=============================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.webviewflutter;

import android.os.Build;
import android.webkit.WebChromeClient;
import androidx.annotation.RequiresApi;
import io.flutter.plugin.common.BinaryMessenger;
import java.util.Arrays;

/**
 * Flutter Api implementation for {@link android.webkit.WebChromeClient.FileChooserParams}.
 *
 * <p>Passes arguments of callbacks methods from a {@link
 * android.webkit.WebChromeClient.FileChooserParams} to Dart.
 */
@RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
public class FileChooserParamsFlutterApiImpl
    extends GeneratedAndroidWebView.FileChooserParamsFlutterApi {
  private final InstanceManager instanceManager;

  /**
   * Creates a Flutter api that sends messages to Dart.
   *
   * @param binaryMessenger handles sending messages to Dart
   * @param instanceManager maintains instances stored to communicate with Dart objects
   */
  public FileChooserParamsFlutterApiImpl(
      BinaryMessenger binaryMessenger, InstanceManager instanceManager) {
    super(binaryMessenger);
    this.instanceManager = instanceManager;
  }

  private static GeneratedAndroidWebView.FileChooserModeEnumData toFileChooserEnumData(int mode) {
    final GeneratedAndroidWebView.FileChooserModeEnumData.Builder builder =
        new GeneratedAndroidWebView.FileChooserModeEnumData.Builder();

    switch (mode) {
      case WebChromeClient.FileChooserParams.MODE_OPEN:
        builder.setValue(GeneratedAndroidWebView.FileChooserMode.OPEN);
        break;
      case WebChromeClient.FileChooserParams.MODE_OPEN_MULTIPLE:
        builder.setValue(GeneratedAndroidWebView.FileChooserMode.OPEN_MULTIPLE);
        break;
      case WebChromeClient.FileChooserParams.MODE_SAVE:
        builder.setValue(GeneratedAndroidWebView.FileChooserMode.SAVE);
        break;
      default:
        throw new IllegalArgumentException(String.format("Unsupported FileChooserMode: %d", mode));
    }

    return builder.build();
  }

  /**
   * Stores the FileChooserParams instance and notifies Dart to create a new FileChooserParams
   * instance that is attached to this one.
   *
   * @return the instanceId of the stored instance
   */
  public long create(WebChromeClient.FileChooserParams instance, Reply<Void> callback) {
    final long instanceId = instanceManager.addHostCreatedInstance(instance);
    create(
        instanceId,
        instance.isCaptureEnabled(),
        Arrays.asList(instance.getAcceptTypes()),
        toFileChooserEnumData(instance.getMode()),
        instance.getFilenameHint(),
        callback);
    return instanceId;
  }
}


