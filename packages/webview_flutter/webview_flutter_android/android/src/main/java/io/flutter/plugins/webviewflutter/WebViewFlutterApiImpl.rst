packages/webview_flutter/webview_flutter_android/android/src/main/java/io/flutter/plugins/webviewflutter/WebViewFlutterApiImpl.java
===================================================================================================================================

Last edited: 2023-03-17 07:52:27

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.webviewflutter;

import android.webkit.WebView;
import androidx.annotation.NonNull;
import androidx.annotation.VisibleForTesting;
import io.flutter.plugin.common.BinaryMessenger;
import io.flutter.plugins.webviewflutter.GeneratedAndroidWebView.WebViewFlutterApi;

/**
 * Flutter API implementation for `WebView`.
 *
 * <p>This class may handle adding native instances that are attached to a Dart instance or passing
 * arguments of callbacks methods to a Dart instance.
 */
public class WebViewFlutterApiImpl {
  // To ease adding additional methods, this value is added prematurely.
  @SuppressWarnings({"unused", "FieldCanBeLocal"})
  private final BinaryMessenger binaryMessenger;

  private final InstanceManager instanceManager;
  private WebViewFlutterApi api;

  /**
   * Constructs a {@link WebViewFlutterApiImpl}.
   *
   * @param binaryMessenger used to communicate with Dart over asynchronous messages
   * @param instanceManager maintains instances stored to communicate with attached Dart objects
   */
  public WebViewFlutterApiImpl(
      @NonNull BinaryMessenger binaryMessenger, @NonNull InstanceManager instanceManager) {
    this.binaryMessenger = binaryMessenger;
    this.instanceManager = instanceManager;
    api = new WebViewFlutterApi(binaryMessenger);
  }

  /**
   * Stores the `WebView` instance and notifies Dart to create and store a new `WebView` instance
   * that is attached to this one. If `instance` has already been added, this method does nothing.
   */
  public void create(@NonNull WebView instance, @NonNull WebViewFlutterApi.Reply<Void> callback) {
    if (!instanceManager.containsInstance(instance)) {
      api.create(instanceManager.addHostCreatedInstance(instance), callback);
    }
  }

  /**
   * Sets the Flutter API used to send messages to Dart.
   *
   * <p>This is only visible for testing.
   */
  @VisibleForTesting
  void setApi(@NonNull WebViewFlutterApi api) {
    this.api = api;
  }
}


