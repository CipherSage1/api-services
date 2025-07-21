package com.organization.sage.model.organisation;

import com.organization.sage.model.payment.Pricing;

public class PricingRequest {
  private String userId;
  private Pricing pricing;

  public PricingRequest(String userId, Pricing pricing) {
      this.userId = userId;
      this.pricing = pricing;
  }

  public String getUserId() {
      return userId;
  }

  public Pricing getPricing() {
      return pricing;
  }
}
