README.md
=========

Last edited: 2023-03-30 22:19:42

Contents:

.. code-block:: md

    # Beet Swift

Its a port of [Beet](https://github.com/metaplex-foundation/beet/tree/master/beet#features), Strict borsh compatible de/serializer. It can be used as a stand alone library. Its the main serializer for Solita

## Features

It supports 

- fully composable, i.e. `coption(inner: Beet.fixedBeet(.init(value: .scalar(i64()))))` is handled correctly
- structs can be nested and composed
- pre-computes `byteSize` of any fixed size type, no matter how deeply nested or composed it is
- converts non-fixed types to their fixed versions simply by providing a value or serialized
  data
- fixed size and _fixable_ structs expose identical serialize/deserialize API and perform
  conversions under the hood when needed

## Fixed Size vs. Dynamic Types 

Beet is optimized for _fixed_ types as this allows logging detailed diagnostics about the
structure of data that it is processing as well as avoiding Buffer resizes.

Only _beets_ that have _fixed_ in the name are of fixed size, all others are _fixable_ types
which expose `toFixedFromData` and `toFixedFromValue` methods to convert to a _fixed beet_ from
serialized data or a value respectively.

Beet provides the `FixableBeetStruct` to de/serialize arguments (dictionaries) that have non-fixed size fields. 

Beet implements the entire [borsh spec](https://borsh.io/). 

## Examples

### Single Fixed Struct Configuration

```swift
import Beet

struct Results: Equatable {
    let win: UInt8
    let totalWin: UInt16
    let losses: Int32
    
    static let `struct` = BeetStruct(
        fields: [
            ("win", FixedSizeBeet(value: .scalar(u8()))),
            ("totalWin", FixedSizeBeet(value:.scalar(u16()))),
            ("losses", FixedSizeBeet(value: .scalar(i32())))
        ],
        construct: { args in
            Results(
                win: args["win"] as! UInt8,
                totalWin: args["totalWin"] as! UInt16,
                losses: args["losses"] as! Int32
            )
        },
        description: "Results"
    )
}
```

### Nested Struct Configuration

```swift
import Beet
import Solana

struct Trader: Equatable {
    let name: String
    let results: Results
    let age: UInt8
    
    static let `struct` = BeetStruct(
        fields: [
            ("name", FixedSizeBeet(value: .collection(FixedSizeUtf8String(stringByteLength: 4)))),
            ("results", FixedSizeBeet(value:.scalar(Results.struct))),
            ("age", FixedSizeBeet(value: .scalar(u8())))
        ],
        construct: { args in
            Trader(
                name: args["name"] as! String,
                results: args["results"] as! Results,
                age: args["age"] as! UInt8
            )
        },
        description: "Trader"
    )
}

let trader = Trader(name: "bob ", results: Results(win: 20, totalWin: 1200, losses: -455), age: 22)
let (buf,_) = Trader.struct.serialize(instance: trader, byteSize: Int(Trader.struct.byteSize))
let (deserialized, _) = Trader.struct.deserialize(buffer: buf)
```

## LICENSE

Apache-2.0


