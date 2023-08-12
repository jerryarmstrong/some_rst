packages/webview_flutter/webview_flutter_android/android/src/main/java/io/flutter/plugins/webviewflutter/CookieManagerHostApiImpl.java
======================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.webviewflutter;

import android.os.Build;
import android.webkit.CookieManager;

class CookieManagerHostApiImpl implements GeneratedAndroidWebView.CookieManagerHostApi {
  @Override
  public void clearCookies(GeneratedAndroidWebView.Result<Boolean> result) {
    CookieManager cookieManager = CookieManager.getInstance();
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
      cookieManager.removeAllCookies(result::success);
    } else {
      final boolean hasCookies = cookieManager.hasCookies();
      if (hasCookies) {
        cookieManager.removeAllCookie();
      }
      result.success(hasCookies);
    }
  }

  @Override
  public void setCookie(String url, String value) {
    CookieManager.getInstance().setCookie(url, value);
  }
}


