packages/webview_flutter/webview_flutter_android/android/src/test/java/io/flutter/plugins/webviewflutter/WebStorageHostApiImplTest.java
=======================================================================================================================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package io.flutter.plugins.webviewflutter;

import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import android.webkit.WebStorage;
import org.junit.After;
import org.junit.Before;
import org.junit.Rule;
import org.junit.Test;
import org.mockito.Mock;
import org.mockito.junit.MockitoJUnit;
import org.mockito.junit.MockitoRule;

public class WebStorageHostApiImplTest {
  @Rule public MockitoRule mockitoRule = MockitoJUnit.rule();

  @Mock public WebStorage mockWebStorage;

  @Mock WebStorageHostApiImpl.WebStorageCreator mockWebStorageCreator;

  InstanceManager testInstanceManager;
  WebStorageHostApiImpl testHostApiImpl;

  @Before
  public void setUp() {
    testInstanceManager = InstanceManager.open(identifier -> {});

    when(mockWebStorageCreator.createWebStorage()).thenReturn(mockWebStorage);
    testHostApiImpl = new WebStorageHostApiImpl(testInstanceManager, mockWebStorageCreator);
    testHostApiImpl.create(0L);
  }

  @After
  public void tearDown() {
    testInstanceManager.close();
  }

  @Test
  public void deleteAllData() {
    testHostApiImpl.deleteAllData(0L);
    verify(mockWebStorage).deleteAllData();
  }
}


