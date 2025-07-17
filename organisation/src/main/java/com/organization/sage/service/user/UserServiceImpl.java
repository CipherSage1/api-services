package com.organization.sage.service.user;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.ParameterizedTypeReference;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import com.organization.sage.model.ApiResponse;
import com.organization.sage.model.user.UserModel;

@Service
public class UserServiceImpl implements UserService {

    private final RestTemplate restTemplate = new RestTemplate();

    @Value("${USER_ORDER_URL}")
    private String USER_ORDER_URL;

    @Value("${USER_ORDER_URL_API_KEY}")
    private String USER_ORDER_URL_API_KEY;

    public ApiResponse<UserModel> updateUserPartially(String id, UserModel updates) {
        String baseUrl = USER_ORDER_URL + "/api/v1/internal-ops/user-update/" + id;

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON); 
        headers.set("Api_Key",  USER_ORDER_URL_API_KEY);
        HttpEntity<UserModel> requestEntity = new HttpEntity<>(updates, headers);

        ResponseEntity<ApiResponse<UserModel>> response = restTemplate.exchange(
                baseUrl,
                HttpMethod.PUT,
                requestEntity,
                new ParameterizedTypeReference<ApiResponse<UserModel>>() {
                });

        return response.getBody();
    }
   
}
