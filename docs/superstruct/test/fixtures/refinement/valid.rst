test/fixtures/refinement/valid.ts
=================================

Last edited: 2020-08-13 15:30:25

Contents:

.. code-block:: ts

    import isEmail from 'is-email'
import { string, refinement } from '../../..'

export const Struct = refinement(string(), 'Email', isEmail)

export const data = 'name@example.com'

export const output = 'name@example.com'


