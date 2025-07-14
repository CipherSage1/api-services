package com.organization.sage.service.organization;

import com.organization.sage.model.organisation.Organization;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.UUID;

@Service
public class OrganizationServiceImpl implements OrganizationService {

    private final RestTemplate restTemplate = new RestTemplate();

    @Value("${BASE_URL}"+"/organizations")
    private String jsonServerUrl;

    @Override
    public Organization createOrganization(Organization org) {
        org.setOrganizationId(UUID.randomUUID().toString());
        ResponseEntity<Organization> response = restTemplate.postForEntity(jsonServerUrl, org, Organization.class);
        return response.getBody();
    }

    @Override
    public List<Organization> getAllOrganizations() {
        ResponseEntity<Organization[]> response = restTemplate.getForEntity(jsonServerUrl, Organization[].class);
        return Arrays.asList(response.getBody());
    }

    @Override
    public Organization getOrganizationById(String id) {
        String url = jsonServerUrl + "/" + id;
        return restTemplate.getForObject(url, Organization.class);
    }

    @Override
    public void updateOrganization(String id, Organization org) {
        String url = jsonServerUrl + "/" + id;
        restTemplate.put(url, org);
    }

    @Override
    public void updateOrganizationPartially(String id, Map<String, Object> updates) {
        String url = jsonServerUrl + "/" + id;
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        HttpEntity<Map<String, Object>> request = new HttpEntity<>(updates, headers);
        restTemplate.exchange(url, HttpMethod.PATCH, request, Void.class);
    }

    @Override
    public void deleteOrganization(String id) {
        String url = jsonServerUrl + "/" + id;
        restTemplate.delete(url);
    }
}
