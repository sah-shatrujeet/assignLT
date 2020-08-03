module "ec2_instance" {
  source                            =  "../modules/ec2_instance/"
  ec2                               =  [
    {
      ami_id                        =  "ami-0ac80df6eff0e70b5"##"ami-03e33d201c4eabe91"
      instance_type                 =  "t2.large"
      key_name                      =  "kundan_useast1"
      subnet                        =  "subnet-0fb88431"
      security_groups               =  ["sg-042d3bcf20c6a01e9"]
    }
  ]
  tags                              =  {
    Environment                     =  "Demo"
    Name                            =  "elk"
  }
}
