README.md
=========

Last edited: 2022-11-21 17:18:33

Contents:

.. code-block:: md

    # kBorsh

## Borsh Kotlin Serialization Format

This library provides a Borsh serialization format for kotlinx-serialization.

## Installation

### JitPack [![Release](https://jitpack.io/v/metaplex-foundation/metaplex-android.svg)](https://jitpack.io/#metaplex-foundation/metaplex-android)

Android (and possibly JVM) projects can install the library through [JitPack.io](https://jitpack.io/#metaplex-foundation/metaplex-android)

First, add the JitPack repository to your build:

```
repositories {
    ...
    maven { url 'https://jitpack.io' }
}
```

Then add the dependency to the 'build.gradle' file for your app/module:

```
dependencies {
    ...
    implementation 'com.github.metaplex-foundation:kborsh:{version}'
}
```

### Using GitHub Packages

Jitpack only publishes Android libraries. To access the full multiplatform build, the library must be downloaded as a GitHub Package.

First, add the Github Packages Maven repository to your build:

```
repositories {
    ...
    // can add other repos to this array if needed
    ["/metaplex-foundation/kborsh"].forEach { path ->
        maven {
            setName("github")
            setUrl("https://maven.pkg.github.com${path}")
            credentials(PasswordCredentials)
        }
    }
}
```

Then add the dependency to the 'build.gradle' file for your app/module:

```
dependencies {
    ...
    implementation 'com.metaplex:kborsh:{version}'
}
```

Somewhere in your environment you will need to add the following properties for GitHub authentication:

```
githubUsername={your GitHub username}
githubPassword={valid GitHub token for your account}
```

## Usage

```kotlin
@Serializable
data class MyObject(val name: String, val id: Int, val price: Float)

// given a serializable object
val myObject = MyObject("Some Thing", 1234, 567.89f)

// encode it as bytes according to the Borsh.io specification
val myObjectBorshEncoded: ByteArray = Borsh.encodeToByteArray(myObject)

// decode serializable object from bytes
val myObjectDecoded: MyObject = Borsh.decodeFromByteArray<MyObject>(myObjectBorshEncoded)
```

### From Hex String
```kotlin
@Serializable
data class MyObject(val name: String, val id: Int, val price: Float)

// given a Borsh encoded hex string
val myEncodedString = "0a000000536f6d65205468696e67d2040000f6f80d44"

// decode serializable object from string
val myObjectDecodedFromString: MyObject = Borsh.decodeFromHexString<MyObject>(myObjectBorshEncodedString)
```

### From Base64
```kotlin
@Serializable
data class MyObject(val name: String, val id: Int, val price: Float)

// given a Borsh encoded Base64 string
val myEncodedBase64String = "CgAAAFNvbWUgVGhpbmfSBAAA9vgNRA=="

// can use any Base64 decoder you choose
val encodedBorshBytes: ByteArray = Base64.getDecoder().decode(myEncodedBase64String)

// decode serializable object from bytes
val myObjectDecoded: MyObject = Borsh.decodeFromByteArray<MyObject>(encodedBorshBytes)
```

