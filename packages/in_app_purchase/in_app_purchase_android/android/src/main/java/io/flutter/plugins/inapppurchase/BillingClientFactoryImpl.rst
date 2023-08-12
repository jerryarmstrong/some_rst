packages/in_app_purchase/in_app_purchase_android/android/src/main/java/io/flutter/plugins/inapppurchase/BillingClientFactoryImpl.java
=====================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.inapppurchase;

import android.content.Context;
import com.android.billingclient.api.BillingClient;
import io.flutter.plugin.common.MethodChannel;

/** The implementation for {@link BillingClientFactory} for the plugin. */
final class BillingClientFactoryImpl implements BillingClientFactory {

  @Override
  public BillingClient createBillingClient(Context context, MethodChannel channel) {
    BillingClient.Builder builder = BillingClient.newBuilder(context).enablePendingPurchases();

    return builder.setListener(new PluginPurchaseListener(channel)).build();
  }
}


