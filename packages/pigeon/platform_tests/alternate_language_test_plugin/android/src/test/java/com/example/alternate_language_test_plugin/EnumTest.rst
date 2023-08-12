packages/pigeon/platform_tests/alternate_language_test_plugin/android/src/test/java/com/example/alternate_language_test_plugin/EnumTest.java
============================================================================================================================================

Last edited: 2023-03-17 07:52:27

Contents:

.. code-block:: java

    // Copyright 2013 The Flutter Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

package com.example.alternate_language_test_plugin;

import static org.junit.Assert.*;

import java.util.ArrayList;
import org.junit.Test;

public class EnumTest {
  @Test
  public void nullValue() {
    Enum.DataWithEnum value = new Enum.DataWithEnum();
    value.setState(null);
    ArrayList<Object> list = value.toList();
    Enum.DataWithEnum readValue = Enum.DataWithEnum.fromList(list);
    assertEquals(value.getState(), readValue.getState());
  }
}


