packages/webview_flutter/webview_flutter_android/android/src/main/java/io/flutter/plugins/webviewflutter/DownloadListenerFlutterApiImpl.java
============================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.webviewflutter;

import android.webkit.DownloadListener;
import io.flutter.plugin.common.BinaryMessenger;
import io.flutter.plugins.webviewflutter.GeneratedAndroidWebView.DownloadListenerFlutterApi;

/**
 * Flutter Api implementation for {@link DownloadListener}.
 *
 * <p>Passes arguments of callbacks methods from a {@link DownloadListener} to Dart.
 */
public class DownloadListenerFlutterApiImpl extends DownloadListenerFlutterApi {
  private final InstanceManager instanceManager;

  /**
   * Creates a Flutter api that sends messages to Dart.
   *
   * @param binaryMessenger handles sending messages to Dart
   * @param instanceManager maintains instances stored to communicate with Dart objects
   */
  public DownloadListenerFlutterApiImpl(
      BinaryMessenger binaryMessenger, InstanceManager instanceManager) {
    super(binaryMessenger);
    this.instanceManager = instanceManager;
  }

  /** Passes arguments from {@link DownloadListener#onDownloadStart} to Dart. */
  public void onDownloadStart(
      DownloadListener downloadListener,
      String url,
      String userAgent,
      String contentDisposition,
      String mimetype,
      long contentLength,
      Reply<Void> callback) {
    onDownloadStart(
        getIdentifierForListener(downloadListener),
        url,
        userAgent,
        contentDisposition,
        mimetype,
        contentLength,
        callback);
  }

  private long getIdentifierForListener(DownloadListener listener) {
    final Long identifier = instanceManager.getIdentifierForStrongReference(listener);
    if (identifier == null) {
      throw new IllegalStateException("Could not find identifier for DownloadListener.");
    }
    return identifier;
  }
}


