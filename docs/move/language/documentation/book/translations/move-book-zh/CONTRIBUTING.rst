language/documentation/book/translations/move-book-zh/CONTRIBUTING.md
=====================================================================

Last edited: 2023-08-11 19:18:44

Contents:

.. code-block:: md

    # Contributing to Move Book Chinese Version

感谢您有兴趣为**《Move Book 中文版》**做出贡献！有很多方法可以做出贡献，我们感谢所有这些方式。

本翻译项目由 [*Move 中文社区（MoveCC）*](https://github.com/move-cc)[发起](https://github.com/move-language/move/issues/353)，并与 [MoveDAO 社区](https://github.com/move-dao)共同初步完善。

目前工作仍在进行中！

欢迎所有对 Move 感兴趣的朋友一起加入到《Move Book 中文版》的翻译工作中。

## 提交 PR 的 Commits 格式

```text
[move-book-zh] 关于这个 PR 的描述信息
```

## 文档规范

请参考：[中文技术文档的写作规范](https://github.com/ruanyf/document-style-guide)

### 断句

本书使用 Markdown 作为源文件，使用 [mdBook](https://github.com/rust-lang/mdBook) 作为渲染引擎。

由于中英文有所区别，换行后渲染引擎会自动追加一个空格。为了优化视觉体验，中文一个段落内不必换行，保持中文的段内容为一个物理行。

英文是由空格分隔的文本，所以不存在上述问题。

### 中英文混排规范

文中出现中英文混排时，中文与英文之间需要添加一个空格。如果英文单词结尾，此时单词与标点符号之间不添加空格。

### 数字规范

数字之间需要添加一个空格，如果数字带有英文单位，那么数字与英文单位之间不能添加空格。如果数字后带有中文单位，需要添加一个空格。

```text
正确：如果一个 1s 的帧被划分为 10 个时隙，每个时隙为 100ms。

错误：如果一个1s的帧被划分为10个时隙，每个时隙为100ms。

错误：如果一个 1 s 的帧被划分为10个时隙，每个时隙为 100 ms。
```

### 逗号问题

英文中，没有顿号这种标点符号，逗号常用分隔并列的句子成分或结构。

英文中，像 `and` 并列词的前面通常会有一个 `,`，但在中文里表示对象之间的并列关系时，`和`的前面不能带逗号。

```text
War, famine, and flood are terrible.
战争, 饥荒和洪水都是很可怕的。
```

### 冒号和逗号的使用场景规范

冒号通常用在“问、答、说、指出、宣布、证明、表明、例如”一类动词后面，表示提起下文。
如果在较短的提示句子中，需要将 `：` 改为 `，`；如果提示内容比较多，则使用 `：` 来提起下文：

示例1，提起的内容短少：

```text
十六进制字符串是以 x 为前缀的带引号的字符串文字，例如x'48656C6C6F210A'
```

示例2，提起的内容多：

```text
在这些情况下，vector 的类型是从元素类型或从动态数组的使用上推断出来的。如果无法推断类型或者只是为了更清楚地表示，则可以显式指定类型：

vector<T>[]: vector<T>
vector<T>[e1, ..., en]: vector<T>
```


