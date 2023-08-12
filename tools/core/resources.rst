tools/core/resources.ts
=======================

Last edited: 2023-08-11 18:13:34

Contents:

.. code-block:: ts

    /// Returns resource path part by replacing prohibited characters like white spaces with '-'
export function getResourcePathPart(name: string | undefined) {
  return name?.replace(' ', '-')
}


