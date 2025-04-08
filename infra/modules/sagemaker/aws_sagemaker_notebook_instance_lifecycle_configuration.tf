resource "aws_sagemaker_notebook_instance_lifecycle_configuration" "ml_notebook_config" {
  name = "ml-notebook-config-${random_id.suffix.hex}"
  on_start = base64encode(<<EOF
#!/bin/bash
echo "Installing additional packages..."
pip install -U scikit-learn pandas matplotlib
EOF
  )
}
