language/documentation/book/translations/move-book-zh/src/coding-conventions.md
===============================================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: md

    # Move 编码约定

本节列出了 Move 团队认为有用的一些基本的 Move 编码约定。这些只是建议，如果你喜欢其他格式指南和约定，你可以随时使用它们。

## 命名

- **模块名称**：应该使用小写的蛇形命名法，例如：`fixed_point32`、`vector`。
- **类型名称**：如果不是原生数据类型，则应使用驼峰命名法，例如：`Coin`、`RoleId`。
- **函数名称**：应该使用小写的蛇形命名法，例如：`destroy_empty`。
- **常量名称**：应该使用大写的蛇形命名法，例如：`REQUIRES_CAPABILITY`。
- 泛型类型应该具备描述性，当然在适当的情况下也可以是反描述性的，例如：Vector 泛型类型的参数可以是 `T` 或 `Element`。大多数情况下，模块中的“主”类型命名应该与模块名相同，例如：`option::Option`，`fixed_point32::FixedPoint32`。
- **模块文件名称**：应该与模块名相同，例如：`Option.move`。
- **脚本文件名称**：应该使用小写的蛇形命名法，并且应该与脚本中的“主”函数名匹配。
- **混合文件名称**：如果文件包含多个模块和/或脚本，文件命名应该使用小写的蛇形命名法，并且不需要与内部的任何特定模块/脚本名匹配。

## 导入

- 所有模块的 `use` 语句都应该位于模块的顶部。
- 函数应该从声明它们的模块中完全限定地导入和使用, 而不是在顶部导入。
- 类型应该在顶部导入。如果存在名称冲突，应使用 `as` 在本地适当地重命名类型。

例如，如果有一个模块：

```move
module 0x1::foo {
    struct Foo { }
    const CONST_FOO: u64 = 0;
    public fun do_foo(): Foo { Foo{} }
    ...
}
```

此时将被导入并使用：

```move
module 0x1::bar {
    use 0x1::foo::{Self, Foo};

    public fun do_bar(x: u64): Foo {
        if (x == 10) {
            foo::do_foo()
        } else {
            abort 0
        }
    }
    ...
}
```

并且，如果在导入两个模块时存在本地名称冲突：

```move
module other_foo {
    struct Foo {}
    ...
}

module 0x1::importer {
    use 0x1::other_foo::Foo as OtherFoo;
    use 0x1::foo::Foo;
    ...
}
```

## 注释

- 每个模块、结构体和公共函数声明都应该有对应的注释。
- Move 有文档注释 `///`，常规单行注释 `//`，块注释 `/* */`，和块文档注释 `/** */`。

## 格式化

Move 团队计划编写一个自动格式化程序来执行格式化约定。然而，在此期间：

- 除 `script` 和 `address` 块外，其他的内容应使用四个空格的缩进。
- 每行代码，如果超过 100 个字符，应该换行。
- 结构体和常量应该在模块中的所有函数之前声明。


