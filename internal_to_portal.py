group1 = env['ir.model.data']._xmlid_to_res_id('base.group_user', raise_if_not_found=False)
group2 = env['ir.model.data']._xmlid_to_res_id('base.group_portal', raise_if_not_found=False)
records.write({'groups_id': [Command.unlink(group1)]})
records.write({'groups_id': [Command.link(group2)]})
