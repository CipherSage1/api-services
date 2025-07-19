package com.organization.sage.controller;

import java.util.List;
import java.util.Map;

import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.organization.sage.model.ApiResponse;
import com.organization.sage.model.PricingRequest;
import com.organization.sage.model.organisation.Organization; 
import com.organization.sage.service.organization.OrganizationService;

@RestController
@RequestMapping("/api/internal/organizations")
public class OrganizationController {

    private final OrganizationService organizationService;

    public OrganizationController(OrganizationService organizationService) {
        this.organizationService = organizationService;
    }

    @PostMapping
    public ResponseEntity<ApiResponse<Organization>> create(@RequestBody Organization org) {
        return ResponseEntity.ok(organizationService.createOrganization(org));
    }

    @PostMapping("/pricing")
    public ResponseEntity<ApiResponse<Organization>> createPricing(@RequestBody PricingRequest pricing) {
        return ResponseEntity.ok(organizationService.createPricing(pricing));
    }

    @GetMapping
    public ResponseEntity<ApiResponse<List<Organization>>> getAll() {
        return ResponseEntity.ok(organizationService.getAllOrganizations());
    }

    @GetMapping("/{id}")
    public ResponseEntity<ApiResponse<Organization>> getById(@PathVariable String id) {
        return ResponseEntity.ok(organizationService.getOrganizationById(id));
    }

    @PutMapping("/{id}")
    public ResponseEntity<Void> update(@PathVariable String id, @RequestBody Organization org) {
        organizationService.updateOrganization(id, org);
        return ResponseEntity.noContent().build();
    }

    @PatchMapping("/{id}")
    public ResponseEntity<Void> updatePartially(@PathVariable String id, @RequestBody Map<String, Object> updates) {
        organizationService.updateOrganizationPartially(id, updates);
            return ResponseEntity.noContent().build();
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable String id) {
        organizationService.deleteOrganization(id);
        return ResponseEntity.noContent().build();
    }
    
}
