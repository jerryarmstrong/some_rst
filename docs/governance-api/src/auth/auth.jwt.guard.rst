src/auth/auth.jwt.guard.ts
==========================

Last edited: 2023-04-18 16:02:26

Contents:

.. code-block:: ts

    import type { ExecutionContext } from '@nestjs/common';
import { Injectable } from '@nestjs/common';
import { GqlExecutionContext } from '@nestjs/graphql';
import { AuthGuard } from '@nestjs/passport';

/**
 * Requires that the user is authenticated
 */
@Injectable()
export class AuthJwtGuard extends AuthGuard('authJwt') {
  getRequest(context: ExecutionContext) {
    const ctx = GqlExecutionContext.create(context);
    return ctx.getContext().req;
  }
}


