package com.organization.sage.middleware;

import java.util.List;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;

import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;


@Component
public class AuthenticationInterceptor implements HandlerInterceptor {

    @Value("${SERVER_SERVICE_KEY}") 
    private String API_KEY;

      // Define protected paths and methods
    private static final List<ProtectedPath> PROTECTED_PATHS = List.of(
        new ProtectedPath("/api/internal", "POST"),
        new ProtectedPath("/api/internal", "GET"),
        new ProtectedPath("/api/internal", "PUT"),
        new ProtectedPath("/api/internal", "PATCH"),
        new ProtectedPath("/api/sensitive", "POST"),
        new ProtectedPath("/api/sensitive", "GET"),
        new ProtectedPath("/api/sensitive", "PUT"),
        new ProtectedPath("/api/sensitive", "PATCH")
    );

    @Override
    public boolean preHandle(
            @org.springframework.lang.NonNull HttpServletRequest request,
            @org.springframework.lang.NonNull HttpServletResponse response,
            @org.springframework.lang.NonNull Object handler)
            throws Exception { 
        String path = request.getRequestURI();
        String method = request.getMethod();
        for (ProtectedPath protectedPath : PROTECTED_PATHS) {
            if (path.startsWith(protectedPath.path()) && method.equalsIgnoreCase(protectedPath.method())) {
                String apiKey = request.getHeader("Api_Key");
                String jsonResponse = "{"
                + "\"status\": 403,"
                + "\"message\": \"Unauthorized. Access to resource denied!\","
                + "\"error\": true,"
                + "\"data\": null"
                + "}";
                if (apiKey == null || !apiKey.equals(API_KEY)) {
                    response.setStatus(HttpServletResponse.SC_FORBIDDEN);
                    response.setContentType("application/json");
                    response.getWriter().write(jsonResponse);
                    return false;
                }
            }
        }
        return true;
    }
    private record ProtectedPath(String path, String method) {}
}
