package com.organization.sage.advice;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

import com.organization.sage.dto.ErrorResponseDto;
import com.organization.sage.error.OrganizationException;

@ControllerAdvice
public class ErrorExceptionHandler {

    @ExceptionHandler(RuntimeException.class)
    public ResponseEntity<ErrorResponseDto<Object>> handleRuntimeException(RuntimeException ex) {
        ErrorResponseDto<Object> error = new ErrorResponseDto<Object>(
                HttpStatus.INTERNAL_SERVER_ERROR.value(),
                ex.getMessage() != null ? ex.getMessage()
                        : "Internal Server Error. Something went wrong on the server.",
                true,
                null);
        return new ResponseEntity<>(error, HttpStatus.INTERNAL_SERVER_ERROR);
    }
    
    /**
     * Handles OrganizationException specifically.
     *
     * @param ex the OrganizationException to handle
     * @return a ResponseEntity with an ErrorResponseDto containing the error details
     */

    @ExceptionHandler(OrganizationException.class)
    public ResponseEntity<ErrorResponseDto<Object>> handleOrganizationException(OrganizationException ex) {
        ErrorResponseDto<Object> error = new ErrorResponseDto<Object>(
                ex.getStatusCode(),
                ex.getErrorMessage(),
                true,
                null);
        return new ResponseEntity<>(error, HttpStatus.valueOf(ex.getStatusCode()));
    }

}