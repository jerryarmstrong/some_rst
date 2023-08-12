packages/pigeon/platform_tests/alternate_language_test_plugin/android/src/test/java/com/example/alternate_language_test_plugin/NonNullFieldsTest.java
=====================================================================================================================================================

Last edited: 2023-03-17 07:52:27

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package com.example.alternate_language_test_plugin;

import static org.junit.Assert.*;

import com.example.alternate_language_test_plugin.NonNullFields.NonNullFieldSearchRequest;
import java.lang.IllegalStateException;
import org.junit.Test;

public class NonNullFieldsTest {
  @Test
  public void builder() {
    NonNullFieldSearchRequest request =
        new NonNullFieldSearchRequest.Builder().setQuery("hello").build();
    assertEquals(request.getQuery(), "hello");
  }

  @Test(expected = IllegalStateException.class)
  public void builderThrowsIfNull() {
    NonNullFieldSearchRequest request = new NonNullFieldSearchRequest.Builder().build();
  }
}


