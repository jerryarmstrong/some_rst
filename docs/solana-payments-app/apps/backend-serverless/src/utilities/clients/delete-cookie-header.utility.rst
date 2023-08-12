apps/backend-serverless/src/utilities/clients/delete-cookie-header.utility.ts
=============================================================================

Last edited: 2023-08-11 21:51:34

Contents:

.. code-block:: ts

    import { CookieOptions } from './create-cookie-header.utility.js';

export const deleteMerchantAuthCookieHeader = (): string => {
    const domain = process.env.NODE_ENV === 'development' ? 'localhost' : '.solanapay.com';

    const cookieOptions: CookieOptions = {
        maxAge: 0,
        httpOnly: true,
        secure: process.env.NODE_ENV != 'development',
        sameSite: 'strict',
        path: '/',
        domain: domain,
    };

    return `${'Bearer'}=; Max-Age=${cookieOptions.maxAge}; HttpOnly=${cookieOptions.httpOnly ? 'true' : ''};${
        cookieOptions.secure ? ' Secure' : ''
    };  SameSite=${cookieOptions.sameSite}; Path=${cookieOptions.path}; Domain=${cookieOptions.domain};`;
};


