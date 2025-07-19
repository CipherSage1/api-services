package com.organization.sage.service.organization;

import java.util.List;
import java.util.Map;

import com.organization.sage.model.ApiResponse;
import com.organization.sage.model.PricingRequest;
import com.organization.sage.model.organisation.Organization; 

public interface OrganizationService {

	public ApiResponse<Organization> createOrganization(Organization org);
	
	public ApiResponse<List<Organization>> getAllOrganizations();
	
	public ApiResponse<Organization> getOrganizationById(String id);
	
	public void updateOrganization(String id, Organization org);
	
	public void deleteOrganization(String id);

	public void updateOrganizationPartially(String id, Map<String, Object> updates);

	public ApiResponse<Organization> createPricing(PricingRequest pricing);

}