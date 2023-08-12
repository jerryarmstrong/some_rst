packages/espresso/example/README.md
===================================

Last edited: 2023-02-22 00:22:16

Contents:

.. code-block:: md

    # espresso_example

Demonstrates how to use the espresso package.

The espresso package only runs tests on Android. The example runs on iOS, but this is only to keep our continuous integration bots green.

## Getting Started

To run the Espresso tests:

```java
flutter build apk --debug
./gradlew app:connectedAndroidTest
```


