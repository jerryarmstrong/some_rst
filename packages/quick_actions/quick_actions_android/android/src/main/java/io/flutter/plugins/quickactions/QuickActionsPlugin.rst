packages/quick_actions/quick_actions_android/android/src/main/java/io/flutter/plugins/quickactions/QuickActionsPlugin.java
==========================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.quickactions;

import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.content.pm.ShortcutManager;
import android.os.Build;
import io.flutter.embedding.engine.plugins.FlutterPlugin;
import io.flutter.embedding.engine.plugins.activity.ActivityAware;
import io.flutter.embedding.engine.plugins.activity.ActivityPluginBinding;
import io.flutter.plugin.common.BinaryMessenger;
import io.flutter.plugin.common.MethodChannel;
import io.flutter.plugin.common.PluginRegistry.NewIntentListener;

/** QuickActionsPlugin */
public class QuickActionsPlugin implements FlutterPlugin, ActivityAware, NewIntentListener {
  private static final String CHANNEL_ID = "plugins.flutter.io/quick_actions_android";

  private MethodChannel channel;
  private MethodCallHandlerImpl handler;
  private Activity activity;

  /**
   * Plugin registration.
   *
   * <p>Must be called when the application is created.
   */
  @SuppressWarnings("deprecation")
  public static void registerWith(io.flutter.plugin.common.PluginRegistry.Registrar registrar) {
    final QuickActionsPlugin plugin = new QuickActionsPlugin();
    plugin.setupChannel(registrar.messenger(), registrar.context(), registrar.activity());
  }

  @Override
  public void onAttachedToEngine(FlutterPluginBinding binding) {
    setupChannel(binding.getBinaryMessenger(), binding.getApplicationContext(), null);
  }

  @Override
  public void onDetachedFromEngine(FlutterPluginBinding binding) {
    teardownChannel();
  }

  @Override
  public void onAttachedToActivity(ActivityPluginBinding binding) {
    activity = binding.getActivity();
    handler.setActivity(activity);
    binding.addOnNewIntentListener(this);
    onNewIntent(activity.getIntent());
  }

  @Override
  public void onDetachedFromActivity() {
    handler.setActivity(null);
  }

  @Override
  public void onReattachedToActivityForConfigChanges(ActivityPluginBinding binding) {
    binding.removeOnNewIntentListener(this);
    onAttachedToActivity(binding);
  }

  @Override
  public void onDetachedFromActivityForConfigChanges() {
    onDetachedFromActivity();
  }

  @Override
  public boolean onNewIntent(Intent intent) {
    // Do nothing for anything lower than API 25 as the functionality isn't supported.
    if (Build.VERSION.SDK_INT < Build.VERSION_CODES.N_MR1) {
      return false;
    }
    // Notify the Dart side if the launch intent has the intent extra relevant to quick actions.
    if (intent.hasExtra(MethodCallHandlerImpl.EXTRA_ACTION) && channel != null) {
      Context context = activity.getApplicationContext();
      ShortcutManager shortcutManager =
          (ShortcutManager) context.getSystemService(Context.SHORTCUT_SERVICE);
      String shortcutId = intent.getStringExtra(MethodCallHandlerImpl.EXTRA_ACTION);
      channel.invokeMethod("launch", shortcutId);
      shortcutManager.reportShortcutUsed(shortcutId);
    }
    return false;
  }

  private void setupChannel(BinaryMessenger messenger, Context context, Activity activity) {
    channel = new MethodChannel(messenger, CHANNEL_ID);
    handler = new MethodCallHandlerImpl(context, activity);
    channel.setMethodCallHandler(handler);
  }

  private void teardownChannel() {
    channel.setMethodCallHandler(null);
    channel = null;
    handler = null;
  }
}


