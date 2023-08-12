packages/webview_flutter/webview_flutter_android/android/src/test/java/io/flutter/plugins/webviewflutter/WebViewClientTest.java
===============================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.webviewflutter;

import static org.junit.Assert.assertEquals;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import android.net.Uri;
import android.webkit.WebResourceRequest;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import io.flutter.plugins.webviewflutter.WebViewClientHostApiImpl.WebViewClientCompatImpl;
import io.flutter.plugins.webviewflutter.WebViewClientHostApiImpl.WebViewClientCreator;
import java.util.HashMap;
import org.junit.After;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.mockito.Mock;
import org.mockito.junit.MockitoJUnit;
import org.mockito.junit.MockitoRule;

public class WebViewClientTest {
  @Rule public MockitoRule mockitoRule = MockitoJUnit.rule();

  @Mock public WebViewClientFlutterApiImpl mockFlutterApi;

  @Mock public WebView mockWebView;

  @Mock public WebViewClientCompatImpl mockWebViewClient;

  InstanceManager instanceManager;
  WebViewClientHostApiImpl hostApiImpl;
  WebViewClientCompatImpl webViewClient;

  @Before
  public void setUp() {
    instanceManager = InstanceManager.open(identifier -> {});

    instanceManager.addDartCreatedInstance(mockWebView, 0L);

    final WebViewClientCreator webViewClientCreator =
        new WebViewClientCreator() {
          @Override
          public WebViewClient createWebViewClient(WebViewClientFlutterApiImpl flutterApi) {
            webViewClient = (WebViewClientCompatImpl) super.createWebViewClient(flutterApi);
            return webViewClient;
          }
        };

    hostApiImpl =
        new WebViewClientHostApiImpl(instanceManager, webViewClientCreator, mockFlutterApi);
    hostApiImpl.create(1L);
  }

  @After
  public void tearDown() {
    instanceManager.close();
  }

  @Test
  public void onPageStarted() {
    webViewClient.onPageStarted(mockWebView, "https://www.google.com", null);
    verify(mockFlutterApi)
        .onPageStarted(eq(webViewClient), eq(mockWebView), eq("https://www.google.com"), any());
  }

  @Test
  public void onReceivedError() {
    webViewClient.onReceivedError(mockWebView, 32, "description", "https://www.google.com");
    verify(mockFlutterApi)
        .onReceivedError(
            eq(webViewClient),
            eq(mockWebView),
            eq(32L),
            eq("description"),
            eq("https://www.google.com"),
            any());
  }

  @Test
  public void urlLoading() {
    webViewClient.shouldOverrideUrlLoading(mockWebView, "https://www.google.com");
    verify(mockFlutterApi)
        .urlLoading(eq(webViewClient), eq(mockWebView), eq("https://www.google.com"), any());
  }

  @Test
  public void convertWebResourceRequestWithNullHeaders() {
    final Uri mockUri = mock(Uri.class);
    when(mockUri.toString()).thenReturn("");

    final WebResourceRequest mockRequest = mock(WebResourceRequest.class);
    when(mockRequest.getMethod()).thenReturn("method");
    when(mockRequest.getUrl()).thenReturn(mockUri);
    when(mockRequest.isForMainFrame()).thenReturn(true);
    when(mockRequest.getRequestHeaders()).thenReturn(null);

    final GeneratedAndroidWebView.WebResourceRequestData data =
        WebViewClientFlutterApiImpl.createWebResourceRequestData(mockRequest);
    assertEquals(data.getRequestHeaders(), new HashMap<String, String>());
  }

  @Test
  public void setReturnValueForShouldOverrideUrlLoading() {
    final WebViewClientHostApiImpl webViewClientHostApi =
        new WebViewClientHostApiImpl(
            instanceManager,
            new WebViewClientCreator() {
              @Override
              public WebViewClient createWebViewClient(WebViewClientFlutterApiImpl flutterApi) {
                return mockWebViewClient;
              }
            },
            mockFlutterApi);

    instanceManager.addDartCreatedInstance(mockWebViewClient, 0);
    webViewClientHostApi.setSynchronousReturnValueForShouldOverrideUrlLoading(0L, false);

    verify(mockWebViewClient).setReturnValueForShouldOverrideUrlLoading(false);
  }
}


