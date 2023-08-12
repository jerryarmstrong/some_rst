src/resolve-error.ts
====================

Last edited: 2021-12-28 22:07:55

Contents:

.. code-block:: ts

    import { errorCodeFromLogs } from './parse-error'
import * as anchor from './errors/anchor'
import { tokenLendingErrors } from './errors/token-lending'
import {
  ErrorMeta,
  ErrorWithCode,
  ErrorWithLogs,
  MaybeErrorWithCode,
  ResolveErrorFromCode,
} from './types'

// -----------------
// Error Resolver
// -----------------
export class ErrorResolver {
  constructor(private readonly resolveErrorFromCode?: ResolveErrorFromCode) {}

  /**
   * Attempts to resolve the provided error code to a known or custom error.
   *
   * @param captureBoundaryFn is used to exclude everything after (including)
   * that function from the stack trace if possible
   * @param fallbackToUnknown unless `false` a {@link CusperUnknownError} is
   * returned when resolution fails
   */
  errorFromCode(
    code: number,
    captureBoundaryFn?: Function,
    fallbackToUnknown = true
  ): MaybeErrorWithCode {
    // Try specific program errors first since they're more likely
    let err =
      this.resolveErrorFromCode != null ? this.resolveErrorFromCode(code) : null

    if (err != null) {
      return this.passPreparedError(
        err,
        captureBoundaryFn ?? this.errorFromCode
      )
    }

    // Then try errors of known programs
    err = AnchorError.fromCode(code)
    if (err != null) {
      return this.passPreparedError(
        err,
        captureBoundaryFn ?? this.errorFromCode
      )
    }
    err = TokenLendingError.fromCode(code)
    if (err != null) {
      return this.passPreparedError(
        err,
        captureBoundaryFn ?? this.errorFromCode
      )
    }

    if (fallbackToUnknown) {
      err = new CusperUnknownError(
        code,
        'CusperUnknownError',
        'cusper does not know this error'
      )
      return this.passPreparedError(
        err,
        captureBoundaryFn ?? this.errorFromCode
      )
    }
  }

  /**
   * Attempts to parse the error code from the provied logs and then resolve it
   * to a known or custom error.
   * @param fallbackToUnknown unless `false` a {@link CusperUnknownError} is
   * returned when resolution fails
   */
  errorFromProgramLogs(
    logs: string[],
    fallbackToUnknown = true
  ): MaybeErrorWithCode {
    const code = errorCodeFromLogs(logs)
    return code == null
      ? null
      : this.errorFromCode(code, this.errorFromProgramLogs, fallbackToUnknown)
  }

  /**
   * Throws an error that it attempts to resolve from the logs of the provided error.
   * If no error can be resolved it throws a {@link CusperUnknownError} instead
   */
  throwError(error: ErrorWithLogs) {
    const err: ErrorWithCode =
      (error.logs != null && this.errorFromProgramLogs(error.logs, true)) ||
      new CusperUnknownError(
        -1,
        'Error created without logs and thus without error code'
      )
    throw this.passPreparedError(err, this.throwError)
  }

  private passPreparedError(err: ErrorWithCode, captureBoundaryFn: Function) {
    if (err == null) return null
    if (typeof Error.captureStackTrace === 'function') {
      Error.captureStackTrace(err, captureBoundaryFn)
    }
    return err
  }
}

/**
 * Initializes a Custom Program Error Resolver, aka _Cusper_.
 *
 * @param resolveErrorFromCode if provided it will be used to resolve custom
 * errors before falling back to known program errors
 */
export function initCusper(resolveErrorFromCode?: ResolveErrorFromCode) {
  return new ErrorResolver(resolveErrorFromCode)
}

// -----------------
// Unknown Error
// -----------------
/**
 * This error is returned/raised when an error code couldn't be found or resolved to a
 * custom or known error.
 */
export class CusperUnknownError extends Error {
  constructor(readonly code: number, ...params: any[]) {
    super(...params)
    this.name = 'CusperUnknownError'
  }
}

// -----------------
// Custom Program Error
// -----------------
/**
 * Used by implementers to provide their own errors to be resolved by cusper.
 */
export class CustomProgramError extends Error {
  /**
   * Creates an instance of a {@link CustomProgramError}.
   *
   * @param code the error code for which this error was resolved
   * @param name the name of the error
   */
  constructor(readonly code: number, name: string, ...params: any[]) {
    super(...params)
    this.name = `CustomProgramError#${name}`
  }
}

// -----------------
// Anchor
// -----------------
/**
 * An error raised by the anchor program before getting to the actual program
 * implementation.
 */
export class AnchorError extends Error {
  constructor(readonly code: number, name: string, ...params: any[]) {
    super(...params)
    this.name = `AnchorError#${name}`
  }
  static errorMap: Map<number, ErrorMeta> = Object.entries(
    anchor.LangErrorCode
  ).reduce((acc, [key, code]) => {
    acc.set(code, {
      code,
      name: key,
      message: anchor.LangErrorMessage.get(code),
    })
    return acc
  }, new Map())

  static fromCode(code: number): MaybeErrorWithCode {
    const errorMeta = AnchorError.errorMap.get(code)
    return errorMeta != null
      ? new AnchorError(errorMeta.code, errorMeta.name, errorMeta.message)
      : null
  }

  toString() {
    return `${this.name}: ${this.message}`
  }
}

// -----------------
// Token Lending
// -----------------
/**
 * Error raised by the token lending program.
 * Please note that error codes overlap with other _known_ programs as they start at `0`.
 * Thus in some cases they might be wrongly represented and actually not
 * originate from the token lending program.
 */
export class TokenLendingError extends Error {
  constructor(readonly code: number, name: string, ...params: any[]) {
    super(...params)
    this.name = `TokenLendingError#${name}`
  }
  static errorMap = tokenLendingErrors
  static fromCode(code: number): MaybeErrorWithCode {
    const errorMeta = TokenLendingError.errorMap.get(code)
    return errorMeta != null
      ? new TokenLendingError(errorMeta.code, errorMeta.name, errorMeta.message)
      : null
  }

  toString() {
    return `${this.name}: ${this.message}`
  }
}


