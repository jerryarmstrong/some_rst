flang/docs/IORuntimeInternals.md
================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: md

    <!--===- docs/IORuntimeInternals.md

   Part of the LLVM Project, under the Apache License v2.0 with LLVM Exceptions.
   See https://llvm.org/LICENSE.txt for license information.
   SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception

-->

# Fortran I/O Runtime Library Internal Design

```eval_rst
.. contents::
   :local:
```

This note is meant to be an overview of the design of the *implementation*
of the f18 Fortran compiler's runtime support library for I/O statements.

The *interface* to the I/O runtime support library is defined in the
C++ header file `runtime/io-api.h`.
This interface was designed to minimize the amount of complexity exposed
to its clients, which are of course the sequences of calls generated by
the compiler to implement each I/O statement.
By keeping this interface as simple as possible, we hope that we have
lowered the risk of future incompatible changes that would necessitate
recompilation of Fortran codes in order to link with later versions of
the runtime library.
As one will see in `io-api.h`, the interface is also directly callable
from C and C++ programs.

The I/O facilities of the Fortran 2018 language are specified in the
language standard in its clauses 12 (I/O statements) and 13 (`FORMAT`).
It's a complicated collection of language features:
 * Files can comprise *records* or *streams*.
 * Records can be fixed-length or variable-length.
 * Record files can be accessed sequentially or directly (random access).
 * Files can be *formatted*, or *unformatted* raw bits.
 * `CHARACTER` scalars and arrays can be used as if they were
fixed-length formatted sequential record files.
 * Formatted I/O can be under control of a `FORMAT` statement
or `FMT=` specifier, *list-directed* with default formatting chosen
by the runtime, or `NAMELIST`, in which a collection of variables
can be given a name and passed as a group to the runtime library.
 * Sequential records of a file can be partially processed by one
or more *non-advancing* I/O statements and eventually completed by
another.
 * `FORMAT` strings can manipulate the position in the current
record arbitrarily, causing re-reading or overwriting.
 * Floating-point output formatting supports more rounding modes
than the IEEE standard for floating-point arithmetic.

The Fortran I/O runtime support library is written in C++17, and
uses some C++17 standard library facilities, but it is intended
to not have any link-time dependences on the C++ runtime support
library or any LLVM libraries.
This is important because there are at least two C++ runtime support
libraries, and we don't want Fortran application builders to have to
build multiple versions of their codes; neither do we want to require
them to ship LLVM libraries along with their products.

Consequently, dynamic memory allocation in the Fortran runtime
uses only C's `malloc()` and `free()` functions, and the few
C++ standard class templates that we instantiate in the library have been
modified with optional template arguments that override their
allocators and deallocators.

Conversions between the many binary floating-point formats supported
by f18 and their decimal representations are performed with the same
template library of fast conversion algorithms used to interpret
floating-point values in Fortran source programs and to emit them
to module files.

## Overview of Classes

A suite of C++ classes and class templates are composed to construct
the Fortran I/O runtime support library.
They (mostly) reside in the C++ namespace `Fortran::runtime::io`.
They are summarized here in a bottom-up order of dependence.

The header and C++ implementation source file names of these
classes are in the process of being vigorously rearranged and
modified; use `grep` or an IDE to discover these classes in
the source for now.  (Sorry!)

### `Terminator`

A general facility for the entire library, `Terminator` latches a
source program statement location in terms of an unowned pointer to
its source file path name and line number and uses them to construct
a fatal error message if needed.
It is used for both user program errors and internal runtime library crashes.

### `IoErrorHandler`

When I/O error conditions arise at runtime that the Fortran program
might have the privilege to handle itself via `ERR=`, `END=`, or
`EOR=` labels and/or by an `IOSTAT=` variable, this subclass of
`Terminator` is used to either latch the error indication or to crash.
It sorts out priorities in the case of multiple errors and determines
the final `IOSTAT=` value at the end of an I/O statement.

### `MutableModes`

Fortran's formatted I/O statements are affected by a suite of
modes that can be configured by `OPEN` statements, overridden by
data transfer I/O statement control lists, and further overridden
between data items with control edit descriptors in a `FORMAT` string.
These modes are represented with a `MutableModes` instance, and these
are instantiated and copied where one would expect them to be in
order to properly isolate their modifications.
The modes in force at the time each data item is processed constitute
a member of each `DataEdit`.

### `DataEdit`

Represents a single data edit descriptor from a `FORMAT` statement
or `FMT=` character value, with some hidden extensions to also
support formatting of list-directed transfers.
It holds an instance of `MutableModes`, and also has a repetition
count for when an array appears as a data item in the *io-list*.
For simplicity and efficiency, each data edit descriptor is
encoded in the `DataEdit` as a simple capitalized character
(or two) and some optional field widths.

### `FormatControl<>`

This class template traverses a `FORMAT` statement's contents (or `FMT=`
character value) to extract data edit descriptors like `E20.14` to
serve each item in an I/O data transfer statement's *io-list*,
making callbacks to an instance of its class template argument
along the way to effect character literal output and record
positioning.
The Fortran language standard defines formatted I/O as if the `FORMAT`
string were driving the traversal of the data items in the *io-list*,
but our implementation reverses that perspective to allow a more
convenient (for the compiler) I/O runtime support library API design
in which each data item is presented to the library with a distinct
type-dependent call.

Clients of `FormatControl` instantiations call its `GetNextDataEdit()`
member function to acquire the next data edit descriptor to be processed
from the format, and `FinishOutput()` to flush out any remaining
output strings or record positionings at the end of the *io-list*.

The `DefaultFormatControlCallbacks` structure summarizes the API
expected by `FormatControl` from its class template actual arguments.

### `OpenFile`

This class encapsulates all (I hope) the operating system interfaces
used to interact with the host's filesystems for operations on
external units.
Asynchronous I/O interfaces are faked for now with synchronous
operations and deferred results.

### `ConnectionState`

An active connection to an external or internal unit maintains
the common parts of its state in this subclass of `ConnectionAttributes`.
The base class holds state that should not change during the
lifetime of the connection, while the subclass maintains state
that may change during I/O statement execution.

### `InternalDescriptorUnit`

When I/O is being performed from/to a Fortran `CHARACTER` array
rather than an external file, this class manages the standard
interoperable descriptor used to access its elements as records.
It has the necessary interfaces to serve as an actual argument
to the `FormatControl` class template.

### `FileFrame<>`

This CRTP class template isolates all of the complexity involved between
an external unit's `OpenFile` and the buffering requirements
imposed by the capabilities of Fortran `FORMAT` control edit
descriptors that allow repositioning within the current record.
Its interface enables its clients to define a "frame" (my term,
not Fortran's) that is a contiguous range of bytes that are
or may soon be in the file.
This frame is defined as a file offset and a byte size.
The `FileFrame` instance manages an internal circular buffer
with two essential guarantees:

1. The most recently requested frame is present in the buffer
and contiguous in memory.
1. Any extra data after the frame that may have been read from
the external unit will be preserved, so that it's safe to
read from a socket, pipe, or tape and not have to worry about
repositioning and rereading.

In end-of-file situations, it's possible that a request to read
a frame may come up short.

As a CRTP class template, `FileFrame` accesses the raw filesystem
facilities it needs from `*this`.

### `ExternalFileUnit`

This class mixes in `ConnectionState`, `OpenFile`, and
`FileFrame<ExternalFileUnit>` to represent the state of an open
(or soon to be opened) external file descriptor as a Fortran
I/O unit.
It has the contextual APIs required to serve as a template actual
argument to `FormatControl`.
And it contains a `std::variant<>` suitable for holding the
state of the active I/O statement in progress on the unit
(see below).

`ExternalFileUnit` instances reside in a `Map` that is allocated
as a static variable and indexed by Fortran unit number.
Static member functions `LookUp()`, `LookUpOrCrash()`, and `LookUpOrCreate()`
probe the map to convert Fortran `UNIT=` numbers from I/O statements
into references to active units.

### `IoStatementBase`

The subclasses of `IoStatementBase` each encapsulate and maintain
the state of one active Fortran I/O statement across the several
I/O runtime library API function calls it may comprise.
The subclasses handle the distinctions between internal vs. external I/O,
formatted vs. list-directed vs. unformatted I/O, input vs. output,
and so on.

`IoStatementBase` inherits default `FORMAT` processing callbacks and
an `IoErrorHandler`.
Each of the `IoStatementBase` classes that pertain to formatted I/O
support the contextual callback interfaces needed by `FormatControl`,
overriding the default callbacks of the base class, which crash if
called inappropriately (e.g., if a `CLOSE` statement somehow
passes a data item from an *io-list*).

The lifetimes of these subclasses' instances each begin with a user
program call to an I/O API routine with a name like `BeginExternalListOutput()`
and persist until `EndIoStatement()` is called.

To reduce dynamic memory allocation, *external* I/O statements allocate
their per-statement state class instances in space reserved in the
`ExternalFileUnit` instance.
Internal I/O statements currently use dynamic allocation, but
the I/O API supports a means whereby the code generated for the Fortran
program may supply stack space to the I/O runtime support library
for this purpose.

### `IoStatementState`

F18's Fortran I/O runtime support library defines and implements an API
that uses a sequence of function calls to implement each Fortran I/O
statement.
The state of each I/O statement in progress is maintained in some
subclass of `IoStatementBase`, as noted above.
The purpose of `IoStatementState` is to provide generic access
to the specific state classes without recourse to C++ `virtual`
functions or function pointers, language features that may not be
available to us in some important execution environments.
`IoStatementState` comprises a `std::variant<>` of wrapped references
to the various possibilities, and uses `std::visit()` to
access them as needed by the I/O API calls that process each specifier
in the I/O *control-list* and each item in the *io-list*.

Pointers to `IoStatementState` instances are the `Cookie` type returned
in the I/O API for `Begin...` I/O statement calls, passed back for
the *control-list* specifiers and *io-list* data items, and consumed
by the `EndIoStatement()` call at the end of the statement.

Storage for `IoStatementState` is reserved in `ExternalFileUnit` for
external I/O units, and in the various final subclasses for internal
I/O statement states otherwise.

Since Fortran permits a `CLOSE` statement to reference a nonexistent
unit, the library has to treat that (expected to be rare) situation
as a weird variation of internal I/O since there's no `ExternalFileUnit`
available to hold its `IoStatementBase` subclass or `IoStatementState`.

## A Narrative Overview Of `PRINT *, 'HELLO, WORLD'`

1. When the compiled Fortran program begins execution at the `main()`
entry point exported from its main program, it calls `ProgramStart()`
with its arguments and environment.
1. The generated code calls `BeginExternalListOutput()` to
start the sequence of calls that implement the `PRINT` statement.
Since the Fortran runtime I/O library has not yet been used in
this process, its data structures are initialized on this
first call, and Fortran I/O units 5 and 6 are connected with
the stadard input and output file descriptors (respectively).
The default unit code is converted to 6 and passed to
`ExternalFileUnit::LookUpOrCrash()`, which returns a reference to
unit 6's instance.
1. We check that the unit was opened for formatted I/O.
1. `ExternalFileUnit::BeginIoStatement<>()` is called to initialize
an instance of `ExternalListIoStatementState<false>` in the unit,
point to it with an `IoStatementState`, and return a reference to
that object whose address will be the `Cookie` for this statement.
1. The generated code calls `OutputAscii()` with that cookie and the
address and length of the string.
1. `OutputAscii()` confirms that the cookie corresponds to an output
statement and determines that it's list-directed.
1. `ListDirectedStatementState<false>::EmitLeadingSpaceOrAdvance()`
emits the required initial space on the new current output record
by calling `IoStatementState::GetConnectionState()` to locate
the connection state, determining from the record position state
that the space is necessary, and calling `IoStatementState::Emit()`
to cough it out.  That call is redirected to `ExternalFileUnit::Emit()`,
which calls `FileFrame<ExternalFileUnit>::WriteFrame()` to extend
the frame of the current record and then `memcpy()` to fill its
first byte with the space.
1. Back in `OutputAscii()`, the mutable modes and connection state
of the `IoStatementState` are queried to see whether we're in an
`WRITE(UNIT=,FMT=,DELIM=)` statement with a delimited specifier.
If we were, the library would emit the appropriate quote marks,
double up any instances of that character in the text, and split the
text over multiple records if it's long.
1. But we don't have a delimiter, so `OutputAscii()` just carves
up the text into record-sized chunks and emits them.  There's just
one chunk for our short `CHARACTER` string value in this example.
It's passed to `IoStatementState::Emit()`, which (as above) is
redirected to `ExternalFileUnit::Emit()`, which interacts with the
frame to extend the frame and `memcpy` data into the buffer.
1. A flag is set in `ListDirectedStatementState<false>` to remember
that the last item emitted in this list-directed output statement
was an undelimited `CHARACTER` value, so that if the next item is
also an undelimited `CHARACTER`, no interposing space will be emitted
between them.
1. `OutputAscii()` return `true` to its caller.
1. The generated code calls `EndIoStatement()`, which is redirected to
`ExternalIoStatementState<false>`'s override of that function.
As this is not a non-advancing I/O statement, `ExternalFileUnit::AdvanceRecord()`
is called to end the record.  Since this is a sequential formatted
file, a newline is emitted.
1. If unit 6 is connected to a terminal, the buffer is flushed.
`FileFrame<ExternalFileUnit>::Flush()` drives `ExternalFileUnit::Write()`
to push out the data in maximal contiguous chunks, dealing with any
short writes that might occur, and collecting I/O errors along the way.
This statement has no `ERR=` label or `IOSTAT=` specifier, so errors
arriving at `IoErrorHandler::SignalErrno()` will cause an immediate
crash.
1. `ExternalIoStatementBase::EndIoStatement()` is called.
It gets the final `IOSTAT=` value from `IoStatementBase::EndIoStatement()`,
tells the `ExternalFileUnit` that no I/O statement remains active, and
returns the I/O status value back to the program.
1. Eventually, the program calls `ProgramEndStatement()`, which
calls `ExternalFileUnit::CloseAll()`, which flushes and closes all
open files.  If the standard output were not a terminal, the output
would be written now with the same sequence of calls as above.
1. `exit(EXIT_SUCCESS)`.


