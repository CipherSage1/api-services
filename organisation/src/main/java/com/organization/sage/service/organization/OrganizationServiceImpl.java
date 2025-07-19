package com.organization.sage.service.organization;

import com.organization.sage.error.OrganizationException;
import com.organization.sage.model.ApiResponse;
import com.organization.sage.model.LogType;
import com.organization.sage.model.PricingRequest;
import com.organization.sage.model.organisation.Organization;
import com.organization.sage.model.payment.Pricing; 
import com.organization.sage.service.user.UserService;
import com.organization.sage.utility.Logger;
 

import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Map; 

@Service
public class OrganizationServiceImpl implements OrganizationService {

    private final RestTemplate restTemplate = new RestTemplate();

    @Value("${BASE_URL}"+"/organizations")
    private String jsonServerUrl;


    private final UserService userService;

    public OrganizationServiceImpl(UserService userService) {
        this.userService = userService;
    }


    @Override
    public ApiResponse<Organization> createOrganization(Organization org) {

        if (org.getClientId() != null) {
            String checkUrl = jsonServerUrl + "?clientId=" + org.getClientId();
            ResponseEntity<Organization[]> existingOrgsResponse = restTemplate.getForEntity(checkUrl,
                    Organization[].class);
            Organization[] existingOrgs = existingOrgsResponse.getBody();
            if (existingOrgs != null && existingOrgs.length > 0) {
                throw new OrganizationException(409, "Client already has an organization registered!");
            }
        }
    
        org.setOrganizationId(new Organization().getOrganizationId());
        ResponseEntity<Organization> response = restTemplate.postForEntity(jsonServerUrl, org, Organization.class);
        Organization responseBody = response.getBody();
        if (responseBody == null) {
            throw new RuntimeException("Failed to create organization");
        }

        Logger.print("ORG_RESPONSE: "+responseBody, LogType.SUCCESS);

        return new ApiResponse<Organization>(
                HttpStatus.CREATED.value(),
                "✅ Organization created successfully",
                false,
                responseBody
        );
    }

    @Override
    public ApiResponse<List<Organization>> getAllOrganizations() {
        ResponseEntity<Organization[]> response = restTemplate.getForEntity(jsonServerUrl, Organization[].class);
        return new ApiResponse<>(
                HttpStatus.OK.value(),
                "✅ Organizations fetched successfully",
                false,
                Arrays.asList(response.getBody())
        );
    }

    @Override
    public ApiResponse<Organization> getOrganizationById(String id) {
        String url = jsonServerUrl + "/" + id;
        var res = restTemplate.getForObject(url, Organization.class);

        return new ApiResponse<Organization>(
                HttpStatus.OK.value(),
                "✅ Organization fetched successfully",
                false,
                res
        );
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

    @Override
    public ApiResponse<Organization> createPricing(PricingRequest pricing) {
        if (pricing.getUserId() != null) {
            String checkUrl = jsonServerUrl + "?clientId=" + pricing.getUserId();
            ResponseEntity<Organization[]> existingOrgsResponse = restTemplate.getForEntity(checkUrl,
                    Organization[].class);
            Organization[] existingOrgs = existingOrgsResponse.getBody();
            if (existingOrgs != null && existingOrgs.length > 0) {
        
                Organization org = existingOrgs[0];
               
                if (org.getPricing() == null) {
                    var price_array = new ArrayList<Pricing>();
                    price_array.add(pricing.getPricing());
                    org.setPricing(price_array);
                    Logger.print("price_array: " + price_array.toString(), LogType.SUCCESS);
                } else {

                    var isUpdate = false;

                    for (Pricing price : org.getPricing()) {
                        if (price.getFromLocation().equalsIgnoreCase(pricing.getPricing().getFromLocation()) &&
                                pricing.getPricing().getToLocation()
                                        .equalsIgnoreCase(pricing.getPricing().getToLocation())) {
                            price.setShipmentTypesPricing(pricing.getPricing().getShipmentTypesPricing());
                            price.setparcelTypesPricing(pricing.getPricing().getparcelTypesPricing());
                            isUpdate = true;
                        }
                    }
                    if (!isUpdate) {
                        org.getPricing().add(pricing.getPricing());
                    }

                }
                restTemplate.put(jsonServerUrl + "/" + org.getOrganizationId(), org);
                
                Logger.print("price updater for org : "+org, LogType.SUCCESS);
                return new ApiResponse<Organization>(
                        HttpStatus.OK.value(),
                        "✅ Pricing created successfully",
                        false,
                        org
                );
            }
            else {
                throw new OrganizationException(404, "Client does not have an organization registered!");
            }
        } else {
            throw new OrganizationException(400, "User ID is required to create pricing");
        }
    }
}
