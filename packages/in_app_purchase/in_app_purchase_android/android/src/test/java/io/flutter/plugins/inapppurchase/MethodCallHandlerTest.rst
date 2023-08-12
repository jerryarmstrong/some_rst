packages/in_app_purchase/in_app_purchase_android/android/src/test/java/io/flutter/plugins/inapppurchase/MethodCallHandlerTest.java
==================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.inapppurchase;

import static io.flutter.plugins.inapppurchase.InAppPurchasePlugin.MethodNames.ACKNOWLEDGE_PURCHASE;
import static io.flutter.plugins.inapppurchase.InAppPurchasePlugin.MethodNames.CONSUME_PURCHASE_ASYNC;
import static io.flutter.plugins.inapppurchase.InAppPurchasePlugin.MethodNames.END_CONNECTION;
import static io.flutter.plugins.inapppurchase.InAppPurchasePlugin.MethodNames.IS_FEATURE_SUPPORTED;
import static io.flutter.plugins.inapppurchase.InAppPurchasePlugin.MethodNames.IS_READY;
import static io.flutter.plugins.inapppurchase.InAppPurchasePlugin.MethodNames.LAUNCH_BILLING_FLOW;
import static io.flutter.plugins.inapppurchase.InAppPurchasePlugin.MethodNames.LAUNCH_PRICE_CHANGE_CONFIRMATION_FLOW;
import static io.flutter.plugins.inapppurchase.InAppPurchasePlugin.MethodNames.ON_DISCONNECT;
import static io.flutter.plugins.inapppurchase.InAppPurchasePlugin.MethodNames.ON_PURCHASES_UPDATED;
import static io.flutter.plugins.inapppurchase.InAppPurchasePlugin.MethodNames.QUERY_PURCHASES_ASYNC;
import static io.flutter.plugins.inapppurchase.InAppPurchasePlugin.MethodNames.QUERY_PURCHASE_HISTORY_ASYNC;
import static io.flutter.plugins.inapppurchase.InAppPurchasePlugin.MethodNames.QUERY_SKU_DETAILS;
import static io.flutter.plugins.inapppurchase.InAppPurchasePlugin.MethodNames.START_CONNECTION;
import static io.flutter.plugins.inapppurchase.Translator.fromBillingResult;
import static io.flutter.plugins.inapppurchase.Translator.fromPurchaseHistoryRecordList;
import static io.flutter.plugins.inapppurchase.Translator.fromPurchasesList;
import static io.flutter.plugins.inapppurchase.Translator.fromSkuDetailsList;
import static java.util.Arrays.asList;
import static java.util.Collections.singletonList;
import static java.util.Collections.unmodifiableList;
import static java.util.stream.Collectors.toList;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.fail;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.contains;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.ArgumentMatchers.refEq;
import static org.mockito.Mockito.doAnswer;
import static org.mockito.Mockito.doNothing;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.never;
import static org.mockito.Mockito.times;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import android.app.Activity;
import android.content.Context;
import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import com.android.billingclient.api.AcknowledgePurchaseParams;
import com.android.billingclient.api.AcknowledgePurchaseResponseListener;
import com.android.billingclient.api.BillingClient;
import com.android.billingclient.api.BillingClient.SkuType;
import com.android.billingclient.api.BillingClientStateListener;
import com.android.billingclient.api.BillingFlowParams;
import com.android.billingclient.api.BillingResult;
import com.android.billingclient.api.ConsumeParams;
import com.android.billingclient.api.ConsumeResponseListener;
import com.android.billingclient.api.PriceChangeConfirmationListener;
import com.android.billingclient.api.PriceChangeFlowParams;
import com.android.billingclient.api.Purchase;
import com.android.billingclient.api.PurchaseHistoryRecord;
import com.android.billingclient.api.PurchaseHistoryResponseListener;
import com.android.billingclient.api.PurchasesResponseListener;
import com.android.billingclient.api.QueryPurchaseHistoryParams;
import com.android.billingclient.api.QueryPurchasesParams;
import com.android.billingclient.api.SkuDetails;
import com.android.billingclient.api.SkuDetailsParams;
import com.android.billingclient.api.SkuDetailsResponseListener;
import io.flutter.embedding.engine.plugins.activity.ActivityPluginBinding;
import io.flutter.plugin.common.MethodCall;
import io.flutter.plugin.common.MethodChannel;
import io.flutter.plugin.common.MethodChannel.Result;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;
import org.json.JSONException;
import org.junit.Before;
import org.junit.Test;
import org.mockito.ArgumentCaptor;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.mockito.Spy;
import org.mockito.invocation.InvocationOnMock;
import org.mockito.stubbing.Answer;

public class MethodCallHandlerTest {
  private MethodCallHandlerImpl methodChannelHandler;
  private BillingClientFactory factory;
  @Mock BillingClient mockBillingClient;
  @Mock MethodChannel mockMethodChannel;
  @Spy Result result;
  @Mock Activity activity;
  @Mock Context context;
  @Mock ActivityPluginBinding mockActivityPluginBinding;

  @Before
  public void setUp() {
    MockitoAnnotations.openMocks(this);
    factory = (@NonNull Context context, @NonNull MethodChannel channel) -> mockBillingClient;
    methodChannelHandler = new MethodCallHandlerImpl(activity, context, mockMethodChannel, factory);
    when(mockActivityPluginBinding.getActivity()).thenReturn(activity);
  }

  @Test
  public void invalidMethod() {
    MethodCall call = new MethodCall("invalid", null);
    methodChannelHandler.onMethodCall(call, result);
    verify(result, times(1)).notImplemented();
  }

  @Test
  public void isReady_true() {
    mockStartConnection();
    MethodCall call = new MethodCall(IS_READY, null);
    when(mockBillingClient.isReady()).thenReturn(true);
    methodChannelHandler.onMethodCall(call, result);
    verify(result).success(true);
  }

  @Test
  public void isReady_false() {
    mockStartConnection();
    MethodCall call = new MethodCall(IS_READY, null);
    when(mockBillingClient.isReady()).thenReturn(false);
    methodChannelHandler.onMethodCall(call, result);
    verify(result).success(false);
  }

  @Test
  public void isReady_clientDisconnected() {
    MethodCall disconnectCall = new MethodCall(END_CONNECTION, null);
    methodChannelHandler.onMethodCall(disconnectCall, mock(Result.class));
    MethodCall isReadyCall = new MethodCall(IS_READY, null);

    methodChannelHandler.onMethodCall(isReadyCall, result);

    verify(result).error(contains("UNAVAILABLE"), contains("BillingClient"), any());
    verify(result, never()).success(any());
  }

  @Test
  public void startConnection() {
    ArgumentCaptor<BillingClientStateListener> captor = mockStartConnection();
    verify(result, never()).success(any());
    BillingResult billingResult =
        BillingResult.newBuilder()
            .setResponseCode(100)
            .setDebugMessage("dummy debug message")
            .build();
    captor.getValue().onBillingSetupFinished(billingResult);

    verify(result, times(1)).success(fromBillingResult(billingResult));
  }

  @Test
  public void startConnection_multipleCalls() {
    Map<String, Object> arguments = new HashMap<>();
    arguments.put("handle", 1);
    MethodCall call = new MethodCall(START_CONNECTION, arguments);
    ArgumentCaptor<BillingClientStateListener> captor =
        ArgumentCaptor.forClass(BillingClientStateListener.class);
    doNothing().when(mockBillingClient).startConnection(captor.capture());

    methodChannelHandler.onMethodCall(call, result);
    verify(result, never()).success(any());
    BillingResult billingResult1 =
        BillingResult.newBuilder()
            .setResponseCode(100)
            .setDebugMessage("dummy debug message")
            .build();
    BillingResult billingResult2 =
        BillingResult.newBuilder()
            .setResponseCode(200)
            .setDebugMessage("dummy debug message")
            .build();
    BillingResult billingResult3 =
        BillingResult.newBuilder()
            .setResponseCode(300)
            .setDebugMessage("dummy debug message")
            .build();

    captor.getValue().onBillingSetupFinished(billingResult1);
    captor.getValue().onBillingSetupFinished(billingResult2);
    captor.getValue().onBillingSetupFinished(billingResult3);

    verify(result, times(1)).success(fromBillingResult(billingResult1));
    verify(result, times(1)).success(any());
  }

  @Test
  public void endConnection() {
    // Set up a connected BillingClient instance
    final int disconnectCallbackHandle = 22;
    Map<String, Object> arguments = new HashMap<>();
    arguments.put("handle", disconnectCallbackHandle);
    MethodCall connectCall = new MethodCall(START_CONNECTION, arguments);
    ArgumentCaptor<BillingClientStateListener> captor =
        ArgumentCaptor.forClass(BillingClientStateListener.class);
    doNothing().when(mockBillingClient).startConnection(captor.capture());
    methodChannelHandler.onMethodCall(connectCall, mock(Result.class));
    final BillingClientStateListener stateListener = captor.getValue();

    // Disconnect the connected client
    MethodCall disconnectCall = new MethodCall(END_CONNECTION, null);
    methodChannelHandler.onMethodCall(disconnectCall, result);

    // Verify that the client is disconnected and that the OnDisconnect callback has
    // been triggered
    verify(result, times(1)).success(any());
    verify(mockBillingClient, times(1)).endConnection();
    stateListener.onBillingServiceDisconnected();
    Map<String, Integer> expectedInvocation = new HashMap<>();
    expectedInvocation.put("handle", disconnectCallbackHandle);
    verify(mockMethodChannel, times(1)).invokeMethod(ON_DISCONNECT, expectedInvocation);
  }

  @Test
  public void querySkuDetailsAsync() {
    // Connect a billing client and set up the SKU query listeners
    establishConnectedBillingClient(/* arguments= */ null, /* result= */ null);
    String skuType = BillingClient.SkuType.INAPP;
    List<String> skusList = asList("id1", "id2");
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("skuType", skuType);
    arguments.put("skusList", skusList);
    MethodCall queryCall = new MethodCall(QUERY_SKU_DETAILS, arguments);

    // Query for SKU details
    methodChannelHandler.onMethodCall(queryCall, result);

    // Assert the arguments were forwarded correctly to BillingClient
    ArgumentCaptor<SkuDetailsParams> paramCaptor = ArgumentCaptor.forClass(SkuDetailsParams.class);
    ArgumentCaptor<SkuDetailsResponseListener> listenerCaptor =
        ArgumentCaptor.forClass(SkuDetailsResponseListener.class);
    verify(mockBillingClient).querySkuDetailsAsync(paramCaptor.capture(), listenerCaptor.capture());
    assertEquals(paramCaptor.getValue().getSkuType(), skuType);
    assertEquals(paramCaptor.getValue().getSkusList(), skusList);

    // Assert that we handed result BillingClient's response
    int responseCode = 200;
    List<SkuDetails> skuDetailsResponse = asList(buildSkuDetails("foo"));
    BillingResult billingResult =
        BillingResult.newBuilder()
            .setResponseCode(100)
            .setDebugMessage("dummy debug message")
            .build();
    listenerCaptor.getValue().onSkuDetailsResponse(billingResult, skuDetailsResponse);
    ArgumentCaptor<HashMap<String, Object>> resultCaptor = ArgumentCaptor.forClass(HashMap.class);
    verify(result).success(resultCaptor.capture());
    HashMap<String, Object> resultData = resultCaptor.getValue();
    assertEquals(resultData.get("billingResult"), fromBillingResult(billingResult));
    assertEquals(resultData.get("skuDetailsList"), fromSkuDetailsList(skuDetailsResponse));
  }

  @Test
  public void querySkuDetailsAsync_clientDisconnected() {
    // Disconnect the Billing client and prepare a querySkuDetails call
    MethodCall disconnectCall = new MethodCall(END_CONNECTION, null);
    methodChannelHandler.onMethodCall(disconnectCall, mock(Result.class));
    String skuType = BillingClient.SkuType.INAPP;
    List<String> skusList = asList("id1", "id2");
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("skuType", skuType);
    arguments.put("skusList", skusList);
    MethodCall queryCall = new MethodCall(QUERY_SKU_DETAILS, arguments);

    // Query for SKU details
    methodChannelHandler.onMethodCall(queryCall, result);

    // Assert that we sent an error back.
    verify(result).error(contains("UNAVAILABLE"), contains("BillingClient"), any());
    verify(result, never()).success(any());
  }

  // Test launchBillingFlow not crash if `accountId` is `null`
  // Ideally, we should check if the `accountId` is null in the parameter; however,
  // since PBL 3.0, the `accountId` variable is not public.
  @Test
  public void launchBillingFlow_null_AccountId_do_not_crash() {
    // Fetch the sku details first and then prepare the launch billing flow call
    String skuId = "foo";
    queryForSkus(singletonList(skuId));
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("sku", skuId);
    arguments.put("accountId", null);
    arguments.put("obfuscatedProfileId", null);
    MethodCall launchCall = new MethodCall(LAUNCH_BILLING_FLOW, arguments);

    // Launch the billing flow
    BillingResult billingResult =
        BillingResult.newBuilder()
            .setResponseCode(100)
            .setDebugMessage("dummy debug message")
            .build();
    when(mockBillingClient.launchBillingFlow(any(), any())).thenReturn(billingResult);
    methodChannelHandler.onMethodCall(launchCall, result);

    // Verify we pass the arguments to the billing flow
    ArgumentCaptor<BillingFlowParams> billingFlowParamsCaptor =
        ArgumentCaptor.forClass(BillingFlowParams.class);
    verify(mockBillingClient).launchBillingFlow(any(), billingFlowParamsCaptor.capture());
    BillingFlowParams params = billingFlowParamsCaptor.getValue();

    // Verify we pass the response code to result
    verify(result, never()).error(any(), any(), any());
    verify(result, times(1)).success(fromBillingResult(billingResult));
  }

  @Test
  public void launchBillingFlow_ok_null_OldSku() {
    // Fetch the sku details first and then prepare the launch billing flow call
    String skuId = "foo";
    String accountId = "account";
    queryForSkus(singletonList(skuId));
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("sku", skuId);
    arguments.put("accountId", accountId);
    arguments.put("oldSku", null);
    MethodCall launchCall = new MethodCall(LAUNCH_BILLING_FLOW, arguments);

    // Launch the billing flow
    BillingResult billingResult =
        BillingResult.newBuilder()
            .setResponseCode(100)
            .setDebugMessage("dummy debug message")
            .build();
    when(mockBillingClient.launchBillingFlow(any(), any())).thenReturn(billingResult);
    methodChannelHandler.onMethodCall(launchCall, result);

    // Verify we pass the arguments to the billing flow
    ArgumentCaptor<BillingFlowParams> billingFlowParamsCaptor =
        ArgumentCaptor.forClass(BillingFlowParams.class);
    verify(mockBillingClient).launchBillingFlow(any(), billingFlowParamsCaptor.capture());
    BillingFlowParams params = billingFlowParamsCaptor.getValue();
    // Verify we pass the response code to result
    verify(result, never()).error(any(), any(), any());
    verify(result, times(1)).success(fromBillingResult(billingResult));
  }

  @Test
  public void launchBillingFlow_ok_null_Activity() {
    methodChannelHandler.setActivity(null);

    // Fetch the sku details first and then prepare the launch billing flow call
    String skuId = "foo";
    String accountId = "account";
    queryForSkus(singletonList(skuId));
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("sku", skuId);
    arguments.put("accountId", accountId);
    MethodCall launchCall = new MethodCall(LAUNCH_BILLING_FLOW, arguments);
    methodChannelHandler.onMethodCall(launchCall, result);

    // Verify we pass the response code to result
    verify(result).error(contains("ACTIVITY_UNAVAILABLE"), contains("foreground"), any());
    verify(result, never()).success(any());
  }

  @Test
  public void launchBillingFlow_ok_oldSku() {
    // Fetch the sku details first and query the method call
    String skuId = "foo";
    String accountId = "account";
    String oldSkuId = "oldFoo";
    queryForSkus(unmodifiableList(asList(skuId, oldSkuId)));
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("sku", skuId);
    arguments.put("accountId", accountId);
    arguments.put("oldSku", oldSkuId);
    MethodCall launchCall = new MethodCall(LAUNCH_BILLING_FLOW, arguments);

    // Launch the billing flow
    BillingResult billingResult =
        BillingResult.newBuilder()
            .setResponseCode(100)
            .setDebugMessage("dummy debug message")
            .build();
    when(mockBillingClient.launchBillingFlow(any(), any())).thenReturn(billingResult);
    methodChannelHandler.onMethodCall(launchCall, result);

    // Verify we pass the arguments to the billing flow
    ArgumentCaptor<BillingFlowParams> billingFlowParamsCaptor =
        ArgumentCaptor.forClass(BillingFlowParams.class);
    verify(mockBillingClient).launchBillingFlow(any(), billingFlowParamsCaptor.capture());
    BillingFlowParams params = billingFlowParamsCaptor.getValue();

    // Verify we pass the response code to result
    verify(result, never()).error(any(), any(), any());
    verify(result, times(1)).success(fromBillingResult(billingResult));
  }

  @Test
  public void launchBillingFlow_ok_AccountId() {
    // Fetch the sku details first and query the method call
    String skuId = "foo";
    String accountId = "account";
    queryForSkus(singletonList(skuId));
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("sku", skuId);
    arguments.put("accountId", accountId);
    MethodCall launchCall = new MethodCall(LAUNCH_BILLING_FLOW, arguments);

    // Launch the billing flow
    BillingResult billingResult =
        BillingResult.newBuilder()
            .setResponseCode(100)
            .setDebugMessage("dummy debug message")
            .build();
    when(mockBillingClient.launchBillingFlow(any(), any())).thenReturn(billingResult);
    methodChannelHandler.onMethodCall(launchCall, result);

    // Verify we pass the arguments to the billing flow
    ArgumentCaptor<BillingFlowParams> billingFlowParamsCaptor =
        ArgumentCaptor.forClass(BillingFlowParams.class);
    verify(mockBillingClient).launchBillingFlow(any(), billingFlowParamsCaptor.capture());
    BillingFlowParams params = billingFlowParamsCaptor.getValue();

    // Verify we pass the response code to result
    verify(result, never()).error(any(), any(), any());
    verify(result, times(1)).success(fromBillingResult(billingResult));
  }

  @Test
  public void launchBillingFlow_ok_Proration() {
    // Fetch the sku details first and query the method call
    String skuId = "foo";
    String oldSkuId = "oldFoo";
    String purchaseToken = "purchaseTokenFoo";
    String accountId = "account";
    int prorationMode = BillingFlowParams.ProrationMode.IMMEDIATE_AND_CHARGE_PRORATED_PRICE;
    queryForSkus(unmodifiableList(asList(skuId, oldSkuId)));
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("sku", skuId);
    arguments.put("accountId", accountId);
    arguments.put("oldSku", oldSkuId);
    arguments.put("purchaseToken", purchaseToken);
    arguments.put("prorationMode", prorationMode);
    MethodCall launchCall = new MethodCall(LAUNCH_BILLING_FLOW, arguments);

    // Launch the billing flow
    BillingResult billingResult =
        BillingResult.newBuilder()
            .setResponseCode(100)
            .setDebugMessage("dummy debug message")
            .build();
    when(mockBillingClient.launchBillingFlow(any(), any())).thenReturn(billingResult);
    methodChannelHandler.onMethodCall(launchCall, result);

    // Verify we pass the arguments to the billing flow
    ArgumentCaptor<BillingFlowParams> billingFlowParamsCaptor =
        ArgumentCaptor.forClass(BillingFlowParams.class);
    verify(mockBillingClient).launchBillingFlow(any(), billingFlowParamsCaptor.capture());
    BillingFlowParams params = billingFlowParamsCaptor.getValue();

    // Verify we pass the response code to result
    verify(result, never()).error(any(), any(), any());
    verify(result, times(1)).success(fromBillingResult(billingResult));
  }

  @Test
  public void launchBillingFlow_ok_Proration_with_null_OldSku() {
    // Fetch the sku details first and query the method call
    String skuId = "foo";
    String accountId = "account";
    String queryOldSkuId = "oldFoo";
    String oldSkuId = null;
    int prorationMode = BillingFlowParams.ProrationMode.IMMEDIATE_AND_CHARGE_PRORATED_PRICE;
    queryForSkus(unmodifiableList(asList(skuId, queryOldSkuId)));
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("sku", skuId);
    arguments.put("accountId", accountId);
    arguments.put("oldSku", oldSkuId);
    arguments.put("prorationMode", prorationMode);
    MethodCall launchCall = new MethodCall(LAUNCH_BILLING_FLOW, arguments);

    // Launch the billing flow
    BillingResult billingResult =
        BillingResult.newBuilder()
            .setResponseCode(100)
            .setDebugMessage("dummy debug message")
            .build();
    when(mockBillingClient.launchBillingFlow(any(), any())).thenReturn(billingResult);
    methodChannelHandler.onMethodCall(launchCall, result);

    // Assert that we sent an error back.
    verify(result)
        .error(
            contains("IN_APP_PURCHASE_REQUIRE_OLD_SKU"),
            contains("launchBillingFlow failed because oldSku is null"),
            any());
    verify(result, never()).success(any());
  }

  @Test
  public void launchBillingFlow_ok_Full() {
    // Fetch the sku details first and query the method call
    String skuId = "foo";
    String oldSkuId = "oldFoo";
    String purchaseToken = "purchaseTokenFoo";
    String accountId = "account";
    int prorationMode = BillingFlowParams.ProrationMode.IMMEDIATE_AND_CHARGE_FULL_PRICE;
    queryForSkus(unmodifiableList(asList(skuId, oldSkuId)));
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("sku", skuId);
    arguments.put("accountId", accountId);
    arguments.put("oldSku", oldSkuId);
    arguments.put("purchaseToken", purchaseToken);
    arguments.put("prorationMode", prorationMode);
    MethodCall launchCall = new MethodCall(LAUNCH_BILLING_FLOW, arguments);

    // Launch the billing flow
    BillingResult billingResult =
        BillingResult.newBuilder()
            .setResponseCode(100)
            .setDebugMessage("dummy debug message")
            .build();
    when(mockBillingClient.launchBillingFlow(any(), any())).thenReturn(billingResult);
    methodChannelHandler.onMethodCall(launchCall, result);

    // Verify we pass the arguments to the billing flow
    ArgumentCaptor<BillingFlowParams> billingFlowParamsCaptor =
        ArgumentCaptor.forClass(BillingFlowParams.class);
    verify(mockBillingClient).launchBillingFlow(any(), billingFlowParamsCaptor.capture());
    BillingFlowParams params = billingFlowParamsCaptor.getValue();

    // Verify we pass the response code to result
    verify(result, never()).error(any(), any(), any());
    verify(result, times(1)).success(fromBillingResult(billingResult));
  }

  @Test
  public void launchBillingFlow_clientDisconnected() {
    // Prepare the launch call after disconnecting the client
    MethodCall disconnectCall = new MethodCall(END_CONNECTION, null);
    methodChannelHandler.onMethodCall(disconnectCall, mock(Result.class));
    String skuId = "foo";
    String accountId = "account";
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("sku", skuId);
    arguments.put("accountId", accountId);
    MethodCall launchCall = new MethodCall(LAUNCH_BILLING_FLOW, arguments);

    methodChannelHandler.onMethodCall(launchCall, result);

    // Assert that we sent an error back.
    verify(result).error(contains("UNAVAILABLE"), contains("BillingClient"), any());
    verify(result, never()).success(any());
  }

  @Test
  public void launchBillingFlow_skuNotFound() {
    // Try to launch the billing flow for a random sku ID
    establishConnectedBillingClient(null, null);
    String skuId = "foo";
    String accountId = "account";
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("sku", skuId);
    arguments.put("accountId", accountId);
    MethodCall launchCall = new MethodCall(LAUNCH_BILLING_FLOW, arguments);

    methodChannelHandler.onMethodCall(launchCall, result);

    // Assert that we sent an error back.
    verify(result).error(contains("NOT_FOUND"), contains(skuId), any());
    verify(result, never()).success(any());
  }

  @Test
  public void launchBillingFlow_oldSkuNotFound() {
    // Try to launch the billing flow for a random sku ID
    establishConnectedBillingClient(null, null);
    String skuId = "foo";
    String accountId = "account";
    String oldSkuId = "oldSku";
    queryForSkus(singletonList(skuId));
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("sku", skuId);
    arguments.put("accountId", accountId);
    arguments.put("oldSku", oldSkuId);
    MethodCall launchCall = new MethodCall(LAUNCH_BILLING_FLOW, arguments);

    methodChannelHandler.onMethodCall(launchCall, result);

    // Assert that we sent an error back.
    verify(result).error(contains("IN_APP_PURCHASE_INVALID_OLD_SKU"), contains(oldSkuId), any());
    verify(result, never()).success(any());
  }

  @Test
  public void queryPurchases_clientDisconnected() {
    // Prepare the launch call after disconnecting the client
    methodChannelHandler.onMethodCall(new MethodCall(END_CONNECTION, null), mock(Result.class));

    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("skuType", SkuType.INAPP);
    methodChannelHandler.onMethodCall(new MethodCall(QUERY_PURCHASES_ASYNC, arguments), result);

    // Assert that we sent an error back.
    verify(result).error(contains("UNAVAILABLE"), contains("BillingClient"), any());
    verify(result, never()).success(any());
  }

  @Test
  public void queryPurchases_returns_success() throws Exception {
    establishConnectedBillingClient(null, null);

    CountDownLatch lock = new CountDownLatch(1);
    doAnswer(
            new Answer() {
              public Object answer(InvocationOnMock invocation) {
                lock.countDown();
                return null;
              }
            })
        .when(result)
        .success(any(HashMap.class));

    ArgumentCaptor<PurchasesResponseListener> purchasesResponseListenerArgumentCaptor =
        ArgumentCaptor.forClass(PurchasesResponseListener.class);
    doAnswer(
            new Answer() {
              public Object answer(InvocationOnMock invocation) {
                BillingResult.Builder resultBuilder =
                    BillingResult.newBuilder()
                        .setResponseCode(BillingClient.BillingResponseCode.OK)
                        .setDebugMessage("hello message");
                purchasesResponseListenerArgumentCaptor
                    .getValue()
                    .onQueryPurchasesResponse(resultBuilder.build(), new ArrayList<Purchase>());
                return null;
              }
            })
        .when(mockBillingClient)
        .queryPurchasesAsync(
            any(QueryPurchasesParams.class), purchasesResponseListenerArgumentCaptor.capture());

    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("skuType", SkuType.INAPP);
    methodChannelHandler.onMethodCall(new MethodCall(QUERY_PURCHASES_ASYNC, arguments), result);

    lock.await(5000, TimeUnit.MILLISECONDS);

    verify(result, never()).error(any(), any(), any());

    ArgumentCaptor<HashMap> hashMapCaptor = ArgumentCaptor.forClass(HashMap.class);
    verify(result, times(1)).success(hashMapCaptor.capture());

    HashMap<String, Object> map = hashMapCaptor.getValue();
    assert (map.containsKey("responseCode"));
    assert (map.containsKey("billingResult"));
    assert (map.containsKey("purchasesList"));
    assert ((int) map.get("responseCode") == 0);
  }

  @Test
  public void queryPurchaseHistoryAsync() {
    // Set up an established billing client and all our mocked responses
    establishConnectedBillingClient(null, null);
    ArgumentCaptor<HashMap<String, Object>> resultCaptor = ArgumentCaptor.forClass(HashMap.class);
    BillingResult billingResult =
        BillingResult.newBuilder()
            .setResponseCode(100)
            .setDebugMessage("dummy debug message")
            .build();
    List<PurchaseHistoryRecord> purchasesList = asList(buildPurchaseHistoryRecord("foo"));
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("skuType", SkuType.INAPP);
    ArgumentCaptor<PurchaseHistoryResponseListener> listenerCaptor =
        ArgumentCaptor.forClass(PurchaseHistoryResponseListener.class);

    methodChannelHandler.onMethodCall(
        new MethodCall(QUERY_PURCHASE_HISTORY_ASYNC, arguments), result);

    // Verify we pass the data to result
    verify(mockBillingClient)
        .queryPurchaseHistoryAsync(any(QueryPurchaseHistoryParams.class), listenerCaptor.capture());
    listenerCaptor.getValue().onPurchaseHistoryResponse(billingResult, purchasesList);
    verify(result).success(resultCaptor.capture());
    HashMap<String, Object> resultData = resultCaptor.getValue();
    assertEquals(fromBillingResult(billingResult), resultData.get("billingResult"));
    assertEquals(
        fromPurchaseHistoryRecordList(purchasesList), resultData.get("purchaseHistoryRecordList"));
  }

  @Test
  public void queryPurchaseHistoryAsync_clientDisconnected() {
    // Prepare the launch call after disconnecting the client
    methodChannelHandler.onMethodCall(new MethodCall(END_CONNECTION, null), mock(Result.class));

    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("skuType", SkuType.INAPP);
    methodChannelHandler.onMethodCall(
        new MethodCall(QUERY_PURCHASE_HISTORY_ASYNC, arguments), result);

    // Assert that we sent an error back.
    verify(result).error(contains("UNAVAILABLE"), contains("BillingClient"), any());
    verify(result, never()).success(any());
  }

  @Test
  public void onPurchasesUpdatedListener() {
    PluginPurchaseListener listener = new PluginPurchaseListener(mockMethodChannel);

    BillingResult billingResult =
        BillingResult.newBuilder()
            .setResponseCode(100)
            .setDebugMessage("dummy debug message")
            .build();
    List<Purchase> purchasesList = asList(buildPurchase("foo"));
    ArgumentCaptor<HashMap<String, Object>> resultCaptor = ArgumentCaptor.forClass(HashMap.class);
    doNothing()
        .when(mockMethodChannel)
        .invokeMethod(eq(ON_PURCHASES_UPDATED), resultCaptor.capture());
    listener.onPurchasesUpdated(billingResult, purchasesList);

    HashMap<String, Object> resultData = resultCaptor.getValue();
    assertEquals(fromBillingResult(billingResult), resultData.get("billingResult"));
    assertEquals(fromPurchasesList(purchasesList), resultData.get("purchasesList"));
  }

  @Test
  public void consumeAsync() {
    establishConnectedBillingClient(null, null);
    ArgumentCaptor<BillingResult> resultCaptor = ArgumentCaptor.forClass(BillingResult.class);
    BillingResult billingResult =
        BillingResult.newBuilder()
            .setResponseCode(100)
            .setDebugMessage("dummy debug message")
            .build();
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("purchaseToken", "mockToken");
    arguments.put("developerPayload", "mockPayload");
    ArgumentCaptor<ConsumeResponseListener> listenerCaptor =
        ArgumentCaptor.forClass(ConsumeResponseListener.class);

    methodChannelHandler.onMethodCall(new MethodCall(CONSUME_PURCHASE_ASYNC, arguments), result);

    ConsumeParams params = ConsumeParams.newBuilder().setPurchaseToken("mockToken").build();

    // Verify we pass the data to result
    verify(mockBillingClient).consumeAsync(refEq(params), listenerCaptor.capture());

    listenerCaptor.getValue().onConsumeResponse(billingResult, "mockToken");
    verify(result).success(resultCaptor.capture());

    // Verify we pass the response code to result
    verify(result, never()).error(any(), any(), any());
    verify(result, times(1)).success(fromBillingResult(billingResult));
  }

  @Test
  public void acknowledgePurchase() {
    establishConnectedBillingClient(null, null);
    ArgumentCaptor<BillingResult> resultCaptor = ArgumentCaptor.forClass(BillingResult.class);
    BillingResult billingResult =
        BillingResult.newBuilder()
            .setResponseCode(100)
            .setDebugMessage("dummy debug message")
            .build();
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("purchaseToken", "mockToken");
    arguments.put("developerPayload", "mockPayload");
    ArgumentCaptor<AcknowledgePurchaseResponseListener> listenerCaptor =
        ArgumentCaptor.forClass(AcknowledgePurchaseResponseListener.class);

    methodChannelHandler.onMethodCall(new MethodCall(ACKNOWLEDGE_PURCHASE, arguments), result);

    AcknowledgePurchaseParams params =
        AcknowledgePurchaseParams.newBuilder().setPurchaseToken("mockToken").build();

    // Verify we pass the data to result
    verify(mockBillingClient).acknowledgePurchase(refEq(params), listenerCaptor.capture());

    listenerCaptor.getValue().onAcknowledgePurchaseResponse(billingResult);
    verify(result).success(resultCaptor.capture());

    // Verify we pass the response code to result
    verify(result, never()).error(any(), any(), any());
    verify(result, times(1)).success(fromBillingResult(billingResult));
  }

  @Test
  public void endConnection_if_activity_detached() {
    InAppPurchasePlugin plugin = new InAppPurchasePlugin();
    plugin.setMethodCallHandler(methodChannelHandler);
    mockStartConnection();
    plugin.onDetachedFromActivity();
    verify(mockBillingClient).endConnection();
  }

  @Test
  public void isFutureSupported_true() {
    mockStartConnection();
    final String feature = "subscriptions";
    Map<String, Object> arguments = new HashMap<>();
    arguments.put("feature", feature);

    BillingResult billingResult =
        BillingResult.newBuilder()
            .setResponseCode(BillingClient.BillingResponseCode.OK)
            .setDebugMessage("dummy debug message")
            .build();

    MethodCall call = new MethodCall(IS_FEATURE_SUPPORTED, arguments);
    when(mockBillingClient.isFeatureSupported(feature)).thenReturn(billingResult);
    methodChannelHandler.onMethodCall(call, result);
    verify(result).success(true);
  }

  @Test
  public void isFutureSupported_false() {
    mockStartConnection();
    final String feature = "subscriptions";
    Map<String, Object> arguments = new HashMap<>();
    arguments.put("feature", feature);

    BillingResult billingResult =
        BillingResult.newBuilder()
            .setResponseCode(BillingClient.BillingResponseCode.FEATURE_NOT_SUPPORTED)
            .setDebugMessage("dummy debug message")
            .build();

    MethodCall call = new MethodCall(IS_FEATURE_SUPPORTED, arguments);
    when(mockBillingClient.isFeatureSupported(feature)).thenReturn(billingResult);
    methodChannelHandler.onMethodCall(call, result);
    verify(result).success(false);
  }

  @Test
  public void launchPriceChangeConfirmationFlow() {
    // Set up the sku details
    establishConnectedBillingClient(null, null);
    String skuId = "foo";
    queryForSkus(singletonList(skuId));

    BillingResult billingResult =
        BillingResult.newBuilder()
            .setResponseCode(BillingClient.BillingResponseCode.OK)
            .setDebugMessage("dummy debug message")
            .build();

    // Set up the mock billing client
    ArgumentCaptor<PriceChangeConfirmationListener> priceChangeConfirmationListenerArgumentCaptor =
        ArgumentCaptor.forClass(PriceChangeConfirmationListener.class);
    ArgumentCaptor<PriceChangeFlowParams> priceChangeFlowParamsArgumentCaptor =
        ArgumentCaptor.forClass(PriceChangeFlowParams.class);
    doNothing()
        .when(mockBillingClient)
        .launchPriceChangeConfirmationFlow(
            any(),
            priceChangeFlowParamsArgumentCaptor.capture(),
            priceChangeConfirmationListenerArgumentCaptor.capture());

    // Call the methodChannelHandler
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("sku", skuId);
    methodChannelHandler.onMethodCall(
        new MethodCall(LAUNCH_PRICE_CHANGE_CONFIRMATION_FLOW, arguments), result);

    // Verify the price change params.
    PriceChangeFlowParams priceChangeFlowParams = priceChangeFlowParamsArgumentCaptor.getValue();
    assertEquals(skuId, priceChangeFlowParams.getSkuDetails().getSku());

    // Set the response in the callback
    PriceChangeConfirmationListener priceChangeConfirmationListener =
        priceChangeConfirmationListenerArgumentCaptor.getValue();
    priceChangeConfirmationListener.onPriceChangeConfirmationResult(billingResult);

    // Verify we pass the response to result
    verify(result, never()).error(any(), any(), any());
    ArgumentCaptor<HashMap> resultCaptor = ArgumentCaptor.forClass(HashMap.class);
    verify(result, times(1)).success(resultCaptor.capture());
    assertEquals(fromBillingResult(billingResult), resultCaptor.getValue());
  }

  @Test
  public void launchPriceChangeConfirmationFlow_withoutActivity_returnsActivityUnavailableError() {
    // Set up the sku details
    establishConnectedBillingClient(null, null);
    String skuId = "foo";
    queryForSkus(singletonList(skuId));

    methodChannelHandler.setActivity(null);

    // Call the methodChannelHandler
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("sku", skuId);
    methodChannelHandler.onMethodCall(
        new MethodCall(LAUNCH_PRICE_CHANGE_CONFIRMATION_FLOW, arguments), result);
    verify(result, times(1)).error(eq("ACTIVITY_UNAVAILABLE"), any(), any());
  }

  @Test
  public void launchPriceChangeConfirmationFlow_withoutSkuQuery_returnsNotFoundError() {
    // Set up the sku details
    establishConnectedBillingClient(null, null);
    String skuId = "foo";

    // Call the methodChannelHandler
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("sku", skuId);
    methodChannelHandler.onMethodCall(
        new MethodCall(LAUNCH_PRICE_CHANGE_CONFIRMATION_FLOW, arguments), result);
    verify(result, times(1)).error(eq("NOT_FOUND"), contains("sku"), any());
  }

  @Test
  public void launchPriceChangeConfirmationFlow_withoutBillingClient_returnsUnavailableError() {
    // Set up the sku details
    String skuId = "foo";

    // Call the methodChannelHandler
    HashMap<String, Object> arguments = new HashMap<>();
    arguments.put("sku", skuId);
    methodChannelHandler.onMethodCall(
        new MethodCall(LAUNCH_PRICE_CHANGE_CONFIRMATION_FLOW, arguments), result);
    verify(result, times(1)).error(eq("UNAVAILABLE"), contains("BillingClient"), any());
  }

  private ArgumentCaptor<BillingClientStateListener> mockStartConnection() {
    Map<String, Object> arguments = new HashMap<>();
    arguments.put("handle", 1);
    MethodCall call = new MethodCall(START_CONNECTION, arguments);
    ArgumentCaptor<BillingClientStateListener> captor =
        ArgumentCaptor.forClass(BillingClientStateListener.class);
    doNothing().when(mockBillingClient).startConnection(captor.capture());

    methodChannelHandler.onMethodCall(call, result);
    return captor;
  }

  private void establishConnectedBillingClient(
      @Nullable Map<String, Object> arguments, @Nullable Result result) {
    if (arguments == null) {
      arguments = new HashMap<>();
      arguments.put("handle", 1);
    }
    if (result == null) {
      result = mock(Result.class);
    }

    MethodCall connectCall = new MethodCall(START_CONNECTION, arguments);
    methodChannelHandler.onMethodCall(connectCall, result);
  }

  private void queryForSkus(List<String> skusList) {
    // Set up the query method call
    establishConnectedBillingClient(/* arguments= */ null, /* result= */ null);
    HashMap<String, Object> arguments = new HashMap<>();
    String skuType = SkuType.INAPP;
    arguments.put("skuType", skuType);
    arguments.put("skusList", skusList);
    MethodCall queryCall = new MethodCall(QUERY_SKU_DETAILS, arguments);

    // Call the method.
    methodChannelHandler.onMethodCall(queryCall, mock(Result.class));

    // Respond to the call with a matching set of Sku details.
    ArgumentCaptor<SkuDetailsResponseListener> listenerCaptor =
        ArgumentCaptor.forClass(SkuDetailsResponseListener.class);
    verify(mockBillingClient).querySkuDetailsAsync(any(), listenerCaptor.capture());
    List<SkuDetails> skuDetailsResponse =
        skusList.stream().map(this::buildSkuDetails).collect(toList());

    BillingResult billingResult =
        BillingResult.newBuilder()
            .setResponseCode(100)
            .setDebugMessage("dummy debug message")
            .build();
    listenerCaptor.getValue().onSkuDetailsResponse(billingResult, skuDetailsResponse);
  }

  private SkuDetails buildSkuDetails(String id) {
    String json =
        String.format(
            "{\"packageName\": \"dummyPackageName\",\"productId\":\"%s\",\"type\":\"inapp\",\"price\":\"$0.99\",\"price_amount_micros\":990000,\"price_currency_code\":\"USD\",\"title\":\"Example title\",\"description\":\"Example description.\",\"original_price\":\"$0.99\",\"original_price_micros\":990000}",
            id);
    SkuDetails details = null;
    try {
      details = new SkuDetails(json);
    } catch (JSONException e) {
      fail("buildSkuDetails failed with JSONException " + e.toString());
    }
    return details;
  }

  private Purchase buildPurchase(String orderId) {
    Purchase purchase = mock(Purchase.class);
    when(purchase.getOrderId()).thenReturn(orderId);
    return purchase;
  }

  private PurchaseHistoryRecord buildPurchaseHistoryRecord(String purchaseToken) {
    PurchaseHistoryRecord purchase = mock(PurchaseHistoryRecord.class);
    when(purchase.getPurchaseToken()).thenReturn(purchaseToken);
    return purchase;
  }
}


