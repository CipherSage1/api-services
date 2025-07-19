package com.organization.sage.dto;

public class ErrorResponseDto<T> {

    private int status;
    private String message;
    private boolean error;
    private T data;

   public ErrorResponseDto(int status, String message, boolean error, T data) {
       this.status = status;
       this.message = message;
       this.error = error;
       this.data = data;
   }

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
    
    @Override
    public String toString() {
        return " { " +
                "status: " + status +
                ", message: '" + message + '\'' +
                ", error: " + error +
                ", data: " + data +
                '}';
    }

}
