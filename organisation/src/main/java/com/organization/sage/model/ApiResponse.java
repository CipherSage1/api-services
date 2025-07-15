package com.organization.sage.model;

public class ApiResponse<T> {
    private int status;
    private String message;
    private boolean error;
    private T data;

    public ApiResponse() {
    }

    public ApiResponse(int status, String message, boolean error, T data) {
        this.status = status;
        this.message = message;
        this.error = error;
        this.data = data;
    }

    // Getters and Setters
    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public boolean isError() {
        return error;
    }

    public void setError(boolean error) {
        this.error = error;
    }

    public T getData() {
        return data;
    }

    public void setData(T data) {
        this.data = data;
    }
}
