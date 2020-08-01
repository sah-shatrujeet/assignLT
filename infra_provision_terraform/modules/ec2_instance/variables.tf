variable "ec2" {
  type                              =  list(object({
    ami_id                          =  string
    instance_type                   =  string
    key_name                        =  string
    subnet                          =  string
    security_groups                 =  list(string)
  }))
  default                           =  [
    {
      ami_id                        =  ""
      instance_type                 =  ""
      key_name                      =  ""
      subnet                        =  ""
      security_groups               =  []
    }
  ]
}

variable "tags" {
  description                       =  "Tags"
  type                              =  map(string)
  default                           =  {
    "Provisioner"                   =  "Terraform"
  }
}