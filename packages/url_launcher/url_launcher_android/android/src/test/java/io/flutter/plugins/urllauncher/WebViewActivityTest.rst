packages/url_launcher/url_launcher_android/android/src/test/java/io/flutter/plugins/urllauncher/WebViewActivityTest.java
========================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.urllauncher;

import static org.junit.Assert.assertEquals;

import java.util.Collections;
import org.junit.Test;

public class WebViewActivityTest {
  @Test
  public void extractHeaders_returnsEmptyMapWhenHeadersBundleNull() {
    assertEquals(WebViewActivity.extractHeaders(null), Collections.emptyMap());
  }
}


